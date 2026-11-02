# A complete binary valuation law and bounded-discrepancy density for Narayana numbers

## Finding

For the Narayana recurrence \(a_0=0\), \(a_1=a_2=1\), and \(a_{n+3}=a_{n+2}+a_n\), all positive-index binary valuations have an explicit classification. There is a unique odd two-adic integer \(\theta\), specified intrinsically in the proof and satisfying \(\theta\equiv698045\pmod{2^{22}}\), such that, for integers \(m\ge0\) and \(0\le r<28\), with \(28m+r>0\),

\[
\nu_2(a_{28m+r})=
\begin{cases}
0,&r\in R_0,\\
1,&r\in R_1,\\
2,&r\in R_2,\\
3,&r=14,\\
3+\nu_2(m+1),&r\in\{20,25,27\},\\
5+\nu_2(m)+\nu_2(m-\theta),&r=0,\ m\ge1,
\end{cases}
\]

where

\[
\begin{aligned}
R_0&=\{1,2,3,5,8,9,10,12,15,16,17,19,22,23,24,26\},\\
R_1&=\{4,7,18,21\},\qquad R_2=\{6,11,13\}.
\end{aligned}
\]

The valuation of \(m-\theta\) is the ordinary two-adic valuation (the largest \(k\) for which \(m\equiv\theta\pmod{2^k}\)). In particular, no evaluation of an infinite series is required to decide any finite valuation: lift \(\theta\) only to the necessary modulus.

For every integer \(t\ge0\), let \(C_t(X)=\#\{1\le n\le X:\nu_2(a_n)=t\}\). Then for **every** integer \(X\ge1\),

\[
\big|C_t(X)-p_t X\big|\le16,
\qquad
p_t=\begin{cases}
4/7,&t=0,\\
1/7,&t=1,\\
3/28,&t=2,\\
5/56,&t=3,\\
3/(28\cdot2^{t-2}),&t\in\{4,5\},\\
11/(28\cdot2^{t-2}),&t\ge6.
\end{cases}
\]

Thus every nonnegative valuation occurs with positive natural density, and the discrepancy bound is uniform **simultaneously in the cutoff and the valuation level**.

## Assumptions and scope

The recurrence is indexed as \(a_0=0,a_1=a_2=1\) (other literature conventions may shift the index). For positive integers \(a_n\), \(\nu_2(a_n)\) denotes the exponent of two dividing \(a_n\). Negative indices are used only as an algebraic device: the recurrence is invertible because its characteristic polynomial has constant term \(-1\). The value \(a_0=0\) is excluded from the finite-valuation theorem. The two-adic root \(\theta\) is defined without any assumption about rationality or algebraicity.

## Proof

**1. Matrix interpolation.** Let

\[
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},\qquad
v=\begin{pmatrix}0\\1\\1\end{pmatrix},\qquad e=(1,0,0).
\]

Then \(a_n=eC^nv\) for all integers \(n\), with negative-index values defined through \(C^{-1}\in\mathrm{GL}_3(\mathbb Z)\). Exact multiplication gives

\[
C^{28}=I+8E,\qquad E=
\begin{pmatrix}
1080&737&1583\\
1583&1080&2320\\
2320&1583&3400
\end{pmatrix}.
\]

For each residue \(r\in\{0,\ldots,27\}\) define the convergent two-adic interpolation

\[
F_r(z)=eC^r\sum_{j\ge0}8^jE^j\binom zj\,v,\qquad z\in\mathbb Z_2.
\]

Because \(\binom zj\in\mathbb Z_2\) and the coefficients tend to zero, convergence is uniform; the binomial identity proves \(F_r(m)=a_{28m+r}\) for integers \(m\ge0\). In particular \(F_r(z)\equiv a_r\pmod8\) uniformly in \(z\). Computing the first twenty-eight recurrence terms modulo eight gives precisely the stated \(R_0,R_1,R_2\); the only remaining nonzero residues are \(14,20,25,27\), all divisible by eight, and \(r=0\).

**2. The four nonzero high-valuation residues.** Direct integer recurrence gives \(a_{14}=88\) and \(a_{42}-a_{14}=3914400\), divisible by 32. In the interpolation of \(F_{14}\), the linear term is divisible by 32 and all higher binomial terms by 64. Consequently \(F_{14}(z)\equiv8\pmod{16}\), proving the constant valuation three.

Extending the recurrence backward gives \(a_{-8}=a_{-3}=a_{-1}=0\). For \(r\in\{20,25,27\}\) this means \(F_r(-1)=a_{r-28}=0\). Expanding around \(z=-1\), with \(w=z+1\), gives

\[
F_r(-1+w)=8w\left[eC^{r-28}Ev+
\sum_{j\ge2}\frac{8^{j-1}}j\,eC^{r-28}E^jv\binom{w-1}{j-1}\right].
\]

The leading bracket coefficient is exactly \(a_r/8\), which is odd because \(a_{20}=872\), \(a_{25}=5896\), and \(a_{27}=12664\). Every summand indexed by \(j\ge2\) is even, since \(\nu_2(8^{j-1}/j)\ge1\). Hence the bracket is a two-adic unit for all \(w\), yielding \(\nu_2(F_r(m))=3+\nu_2(m+1)\).

**3. The zero-residue isometry and its unique root.** Write \(u_j=eE^jv\). Since \(F_0(0)=0\), the binomial identity \(\binom zj/z=\binom{z-1}{j-1}/j\) extends the quotient to a continuous function \(h:\mathbb Z_2\to\mathbb Z_2\) satisfying \(F_0(z)=32z h(z)\). The first two coefficients are exact integers:

\[
\frac{8u_1}{32}=580,\quad
\frac{8^2u_2}{32\cdot2}=12899489,
\]

as follows from \(a_{28}=18560\) and \(a_{56}=825604416\). Therefore

\[
h(z)=580+12899489(z-1)+R(z),\quad
R(z)=\sum_{j\ge3}\frac{8^j u_j}{32j}\binom{z-1}{j-1}.
\]

For any \(x,y\in\mathbb Z_2\) and nonnegative integer \(k\), the identity
\(\binom{x}{k}-\binom{y}{k}
=\sum_{i=1}^k\binom{x-y}{i}\binom{y}{k-i}\)
(with the empty sum zero) gives

\[
\nu_2\left(\binom{x}{k}-\binom{y}{k}\right)
\ge\nu_2(x-y)-\lfloor\log_2 k\rfloor
\quad (k\ge1),
\]

because \(\binom{w}{i}=w\binom{w-1}{i-1}/i\) is two-adically integral after multiplying by \(i/w\). The coefficient at index \(j\ge3\) of \(R\) has valuation at least \(3j-5-\nu_2(j)\), and \(3j-5-\nu_2(j)-\lfloor\log_2(j-1)\rfloor\ge3\). Thus

\[
\nu_2(R(x)-R(y))\ge\nu_2(x-y)+3.
\]

The coefficient \(12899489\) is odd. The ultrametric inequality now gives the **exact isometry**

\[
\nu_2(h(x)-h(y))=\nu_2(x-y)\quad(x\ne y).
\]

Also \(h(z)\equiv z-1\pmod2\). An isometry induces an injection, hence a bijection, on every finite quotient \(\mathbb Z/2^k\mathbb Z\), and the unique solutions of \(h(z)\equiv0\pmod{2^k}\) are compatible. Completeness supplies one and only one \(\theta\in\mathbb Z_2\) with \(h(\theta)=0\), necessarily odd. The isometry gives \(\nu_2(h(m))=\nu_2(m-\theta)\), proving the remaining classification. Successive modular lifting yields \(\theta\equiv698045\pmod{2^{22}}\).

**4. Densities and effective error.** Each fixed residue \(r\pmod{28}\) occupies density \(1/28\). In the three classes \(r\in\{20,25,27\}\), the condition \(\nu_2(m+1)=k\) selects exactly one class modulo \(2^{k+1}\). At \(r=0\), \(\theta\) odd, so for any \(t\ge6\), the condition \(\nu_2(m)+\nu_2(m-\theta)=t-5\) selects exactly two classes modulo \(2^{t-4}\): one even and one odd. These disjoint classes give the displayed probabilities, including the isolated \(r=14\) contribution at level three. Every individual arithmetic progression differs from its natural-density prediction by at most one point in any initial interval. Each valuation level uses at most sixteen such progressions (exactly sixteen at level zero), proving \(\lvert C_t(X)-p_tX\rvert\le16\), uniformly in both variables. The probabilities sum to one by a geometric series.

## Verification

The accompanying executable `verify.py` uses exact integer matrix powers to reconstruct \(C^{28}\), the two leading coefficients of \(h\), and the unique zero of \(h\) modulo \(2^{22}\). It separately builds the recurrence modulo \(2^{32}\) and compares the predicted valuation with all 200,000 positive indices through that cutoff. It checks the limiting-density formulas against the corresponding finite counts for twenty-eight valuation levels. Executing `python3 verify.py` prints `VERIFY_OK` upon success. These finite computations validate the arithmetic and implementation only; the proof of the unrestricted assertions is the analytic argument above.

## Relationship to prior work

Guadalupe's 2021 work gives a complete **three-adic** valuation law for this specific Narayana recurrence, motivating the complementary binary question; it does not state this two-adic law. Sobolewski's 2017 work develops binary valuations for generalized Fibonacci recurrences of different shape. Antony and Barman (2024) provide a broad framework for third-order recurrence valuations and Diophantine consequences, rather than the explicit residue classification and uniform density formula here. Work on regularity of valuation sequences gives related general tools but does not supply this classification. The twenty-eight residue matrix, the exceptional two-adic zero, and the simultaneous bounded-discrepancy result are the specific contribution under comparison.

## Limitations

This result concerns the recurrence and normalization explicitly defined above and the prime two only; the prime three is covered separately in the motivating literature. The two-adic root is characterized uniquely, but its rationality or algebraic nature is not determined. Published generic recurrence theorems may imply parts of the isometry technique, and an unindexed explicit valuation formula could exist. Bibliographic priority is not certified. Computational checks are finite, and independent validation has not been performed.

## References

1. R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187v1 (first posted 2021-12-12), https://arxiv.org/abs/2112.06187 .
2. B. Sobolewski, *The 2-adic valuation of generalized Fibonacci sequences*, arXiv:1702.05819 (2017), https://arxiv.org/abs/1702.05819 .
3. D. Antony and R. Barman, *On the p-adic valuation of third order linear recurrence sequences*, arXiv:2402.18279v1 (first posted 2024-02-28), https://arxiv.org/abs/2402.18279 .
4. B. Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits* (2023), for general recurrence-valuation context.
