# Exact dyadic collision and integrability laws for two powers with \(d\equiv2\pmod4\)

## Finding

For **every** integer \(d\ge6\) with \(d\equiv2\pmod4\), let
\[
R_{d,n}(a)=\#\{(x,y)\in(\mathbb Z/2^n\mathbb Z)^2:x^d+y^d\equiv a\pmod{2^n}\},\qquad
F_{d,n}(a)=2^{-n}R_{d,n}(a).
\]
Here \(n\ge1\) and \(a\) is a residue modulo \(2^n\). For Haar-uniform \(T\in\mathbb Z_2\), the sequence \(F_{d,n}(T\bmod2^n)\) converges almost surely and in \(L^s\) for \(0<s<d/(d-2)\) to the following explicit density:
\[
F_d(z)=\begin{cases}
2^{2+(d-2)j},&z\in2^{dj}(1+8\mathbb Z_2),\\
2^{1+(d-2)j},&z\in2^{dj}(2+8\mathbb Z_2),\\
0,&\text{otherwise},
\end{cases}\qquad j=0,1,2,\ldots.
\]
(The two displayed positive cases specify disjoint sets as \(j\) varies.) Its precise integrability range and its moments are
\[
F_d\in L^s(\mathbb Z_2)\iff 0<s<\frac{d}{d-2},\qquad
\int_{\mathbb Z_2}F_d(z)^s\,dz=
\frac{2^{2s}+2^s}{8\bigl(1-2^{(d-2)s-d}\bigr)}
\quad\left(0<s<\frac{d}{d-2}\right).
\]
For all positive \(s\), the **finite-depth moments** \(M_{d,n}(s)=2^{-n}\sum_{a\bmod2^n}F_{d,n}(a)^s\) satisfy the exact recurrence
\[
M_{d,n}(s)=A_s+q_sM_{d,n-d}(s)\quad(n>d),\qquad
A_s=\frac{2^{2s}+2^s}{8},\quad q_s=2^{(d-2)s-d},
\]
with initial values
\[
M_{d,1}(s)=1,\quad M_{d,2}(s)=\frac{2+2^s}{4},\quad
M_{d,r}(s)=A_s+2^{(r-2)s-r}\quad(3\le r\le d).
\]
In particular, the normalized number of ordered four-tuples satisfying an equality of two sums of \(d\)-th powers is
\[
C_{d,n}=2^{-3n}\#\{(x,y,u,v)\bmod2^n:x^d+y^d\equiv u^d+v^d\pmod{2^n}\}
=M_{d,n}(2).
\]
For \(n=dk+r\) with \(k\ge0\), \(1\le r\le d\), and \(Q=2^{d-4}>1\), one obtains the **exact, all-level collision law**
\[
\boxed{\ C_{d,dk+r}=Q^k C_{d,r}+\frac52\frac{Q^k-1}{Q-1}\ },
\]
where \(C_{d,1}=1\), \(C_{d,2}=3/2\), and \(C_{d,r}=5/2+2^{r-4}\) for \(3\le r\le d\). For example, when \(d=6\), \(C_{6,6k+r}=4^k(C_{6,r}+5/6)-5/6\); the collision count grows geometrically in the dyadic precision, unlike a stable local variance.

## Assumptions and scope

All congruence variables are **ordered**, run independently through complete residue rings, and include zero. The modulus is \(2^n\) with \(n\ge1\). The exponent \(d\) is an arbitrary fixed integer at least six with exactly one factor of two, i.e. \(d\equiv2\pmod4\). Haar measure on \(\mathbb Z_2\) gives measure \(2^{-r}\) to each residue class modulo \(2^r\). The assertion is not about integer representations with size bounds or about other primes.

## Proof

**1. Uniform odd-power image.** The compact unit group admits the standard decomposition \(\mathbb Z_2^\times=\{\pm1\}\times(1+4\mathbb Z_2)\). The map raising to an odd power is an automorphism of \(1+4\mathbb Z_2\), whereas squaring maps that group *onto* \(1+8\mathbb Z_2\). Consequently for every \(d=2m\), \(m\) odd, the \(d\)-th power of a uniformly chosen odd \(2\)-adic unit is **uniform** on \(1+8\mathbb Z_2\). Uniformity follows because a continuous surjective homomorphism of compact groups sends normalized Haar measure to normalized Haar measure. Every even \(x\) has \(x^d\equiv0\pmod{2^d}\).

**2. Three disjoint parity branches.** Let \(X,Y\) be independent Haar-uniform \(2\)-adic integers and \(Z=X^d+Y^d\). Both-even has probability \(1/4\), and \(Z=2^dZ'\) conditionally, where \(Z'\) has the original distribution. Exactly-one-odd has probability \(1/2\); its sum is uniform on \(1+8\mathbb Z_2\), because the odd summand is uniform there and the other \(d\)-th power is divisible by \(2^d\), with \(d\ge6\). Both-odd has probability \(1/4\); the sum of two independent uniform points of \(1+8\mathbb Z_2\) is uniform on \(2+8\mathbb Z_2\). The three supports are disjoint, since \(2^d\mathbb Z_2\) lies in \(8\mathbb Z_2\). No cancellation between odd \(d\)-th powers is possible, because their sum is \(2\pmod8\).

Iterating the both-even branch shows that for each \(j\ge0\), the distribution gives probability \(4^{-j}/2\) to the cylinder \(2^{dj}(1+8\mathbb Z_2)\), and probability \(4^{-j}/4\) to \(2^{dj}(2+8\mathbb Z_2)\). Their Haar measures both equal \(2^{-dj-3}\). Dividing probability by Haar measure yields the two displayed values of \(F_d\). The probability of an infinite both-even chain is \(\lim_{j\to\infty}4^{-j}=0\); hence there is no missing atom at zero. The density integrates to one. In particular the additive support has Haar measure \(1/[4(1-2^{-d})]\).

**3. Exact finite-level fibres.** For a residue \(a\bmod2^n\), \(F_{d,n}(a)\) is \(2^n\) times the probability that \(Z\equiv a\pmod{2^n}\). The parity decomposition from Step 2 gives the *exact*, all-residue recursion:
\[
F_{d,n}(a)=
\begin{cases}
4,&a\equiv1\pmod8,\\
2,&a\equiv2\pmod8,\\
2^{d-2}F_{d,n-d}(a/2^d\bmod2^{n-d}),&n>d,\ 2^d\mid a,\\
2^{n-2},&3\le n\le d,\ a=0,\\
0,&\text{otherwise}
\end{cases}\quad(n\ge3).
\]
For \(n=1\), \(F_{d,1}(0)=F_{d,1}(1)=1\); for \(n=2\), the values at residues \(0,1,2,3\) are \(1,2,1,0\). In the third case the uniform residue-class probability is \((1/4)\Pr\{Z'\equiv a/2^d\pmod{2^{n-d}}\}\), and the normalization multiplies its density by \(2^{d-2}\). In the fourth case all even-even pairs contribute to residue zero. All cases are mutually exclusive.

**4. Moment recurrence and collision number.** Under uniform \(a\bmod2^n\), the first two cylinder branches each contribute \(2^{-3}4^s\) and \(2^{-3}2^s\) to \(M_{d,n}(s)\) for \(n\ge3\). For \(n>d\) the even-even branch, a fraction \(2^{-d}\) of all residues, contributes \(2^{-d}2^{(d-2)s}M_{d,n-d}(s)\). This proves the recurrence. The initial values follow from the explicit fibre list in Step 3. Repeated substitution gives, for \(n=dk+r\), \(1\le r\le d\),
\[
M_{d,n}(s)=q_s^kM_{d,r}(s)+A_s\sum_{i=0}^{k-1}q_s^i.
\]
Setting \(s=2\) yields \(q_2=2^{d-4}\) and \(A_2=5/2\). Finally \(\sum_aR_{d,n}(a)^2\) counts the ordered four-tuples in the statement by grouping pairs according to their common sum, so its normalization is exactly \(M_{d,n}(2)\).

**5. Sharp integrability.** The disjoint cylinders of Step 2 give
\[
\int F_d^s=\sum_{j=0}^\infty 2^{-dj-3}
\left[2^{s(2+(d-2)j)}+2^{s(1+(d-2)j)}\right]
=A_s\sum_{j=0}^\infty q_s^j.
\]
This series converges exactly when \((d-2)s-d<0\), which proves the sharp strict threshold; at equality every term is positive and constant, hence divergence. The functions \(F_{d,n}(T\bmod2^n)\) are the conditional expectations of \(F_d\) given the first \(n\) binary digits (by the exact finite residue probabilities). Thus they converge to \(F_d\) almost surely and in \(L^1\) by the standard martingale convergence theorem. For every fixed \(0<s<d/(d-2)\), choose \(u\) with \(\max(1,s)<u<d/(d-2)\). Jensen's inequality gives \(\sup_n\mathbb E F_{d,n}^u\le\mathbb E F_d^u<\infty\), hence convergence also in \(L^s\). The formula above establishes the displayed finite moments, their limits, and the claimed critical boundary.

## Verification

The independent integer-arithmetic checker `verify.py` reconstructs the power-residue distribution by counting \(d\)-th powers and convolving their multiplicities. It compares **every** normalized fibre with the recursion for \(d=6\) and \(1\le n\le13\), for \(d=10\) and \(1\le n\le11\), for \(d=14\) and \(1\le n\le10\), and for \(d=18\) and \(1\le n\le9\). It separately verifies the exact \(4\)-to-\(1\) odd-unit power map for \(3\le n\le13\), and recomputes each normalized collision count by summing squares. It reported 31,818 comparisons passing. To reproduce: run `python3 verify.py` with Python 3 and no dependencies outside its standard library. Finite checks do not certify the infinite theorem; Steps 1–5 do.

## Relationship to prior work

Mishra, *Intersective Polynomials Arising from Sums of Powers* (online February 25, 2021; arXiv:2103.03439, Theorem 3.3, Section 6, Section 7), treats local **solvability** of power-sum polynomials and, for even exponents, normally uses more than two variables. Its table for exponent six starts at four variables. The present theorem instead computes every two-variable dyadic **fibre multiplicity**, an exact four-variable collision count at every modulus, and its limiting integrability spectrum. These are distinct quantifiers and objects; the claim is not that local solvability of higher-variable forms was unknown.

Browning, *The Polynomial Sieve and Equal Sums of Like Polynomials* (arXiv:1306.6767, Theorem 1.2), studies the global second moment of the integer representation function \(r_f(n)\), not exact target-by-target counts modulo powers of two. The present local collision sequence does not follow from that positive-integer large-box asymptotic. Standard \(2\)-adic unit-group structure and Haar pushforward are used without claiming originality for them. General local zeta rationality does not on its own supply the exact target-by-target two-variable representation numbers or the numerical constants here. Arithmetic for exponent equal to a power of two is outside the claimed range. The possibility of an unlocated earlier equivalent theorem, or of derivation from a more specialized diagonal local-density result, remains a priority risk.

## Limitations

Only the dyadic prime, ordered pairs and the exponent class \(d\equiv2\pmod4\), \(d\ge6\), are covered. No corresponding formula is asserted for odd exponents, powers of two, mixed exponents, or sums of three or more powers. An infinite \(L^2\) norm means growth of the normalized collision constants; it does not mean that any finite residue count is infinite. The theorem is proved analytically; exact experiments only corroborate the stated finite-depth identities. No independent audit or publication-priority certification is asserted.

## References

1. B. Mishra, *Intersective Polynomials Arising from Sums of Powers*, Communications in Algebra **49** (2021), 2633–2644. DOI: 10.1080/00927872.2021.1879827. Open preprint: arXiv:2103.03439.
2. T. D. Browning, *The Polynomial Sieve and Equal Sums of Like Polynomials*, arXiv:1306.6767, Theorem 1.2.
3. Standard decomposition of the \(2\)-adic unit group and Haar measure on compact groups; these algebraic facts are explicitly applied in the proof.
