# Exact finite-time footrule noise and a universal overshoot in random-transposition equilibration

## Finding

For every integer \(n\ge4\), start the random-transposition walk on \(S_n\) at the identity. At each integer step, choose two indices independently and uniformly from \(\{1,\ldots,n\}\) and exchange their cards; choosing the same index does nothing. For the permutation \(\pi_t\) after \(t\ge0\) steps, define the absolute-displacement (Spearman-footrule) observable
\[
F_t=\sum_{i=1}^n|\pi_t(i)-i|.
\]
Set
\[
a_n=1-\frac2n,\qquad c_n=1-\frac4n,\qquad
m_n=\frac{n^2-1}{3},\qquad v_n=\frac{(n+1)(2n^2+7)}{45}.
\]
Its exact finite-time mean and variance are
\[
\mathbb E F_t=m_n(1-a_n^t)
\]
and
\[
\boxed{\begin{aligned}
\operatorname{Var}(F_t)={}&v_n+\frac{4(n^2-1)(n+2)}{45}a_n^t\\
&-\frac{(n+1)(3n^3+9n^2-4n+10)}{90}a_n^{2t}
+\frac{(n^2-1)(n^2-4)}{30}c_n^t.
\end{aligned}}
\]
Here \(c_n^0=1\), including the case \(n=4\). At every fixed \(n\ge4\), the variance starts at zero but eventually exceeds its stationary value \(v_n\) and converges to it **from above**. Thus its equilibration is nonmonotone even though its mean increases monotonically.

For every fixed \(s\ge0\), put \(t_n=\lfloor sn/2\rfloor\). Then
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Var}(F_{t_n})}{n^3}
=V(s):=\frac{2+4e^{-s}-(6+3s)e^{-2s}}{45}.}
\]
This function has a unique maximizer \(s_*>0\), determined by
\[
4e^{s_*}=9+6s_*,\qquad s_*=1.506112985339\ldots.
\]
The peak is \(V(s_*)/(2/45)=1.1848837700805\ldots\), an asymptotic \(18.488377\ldots\%\) variance overshoot. It occurs at \(t\sim0.75305649267\,n\), strictly earlier than the global total-variation mixing scale \(n\log n/2\).

## Assumptions and scope

This is a **discrete-time**, uniform-independent-index, lazy random-transposition walk started from the ordered configuration, with distinct cards and fixed positions. The theorem applies to all integers \(n\ge4\) and \(t\ge0\). The normalization is unscaled absolute displacement, not squared displacement, inversion count, normalized footrule correlation, continuous-time Poissonization, or quantum-walk probability. The large-deck claim concerns \(t_n=\lfloor sn/2\rfloor\) for fixed \(s\), followed by taking the maximum of the deterministic limiting curve; it does not assert a uniform-in-\(s\) finite-deck error rate or a unique finite-deck maximizing time.

## Proof

**1. Exact mean.** The one-card permutation module is the sum of the trivial and standard representations. The random-transposition transition has eigenvalues \(1\) and \(a_n=1-2/n\) there. Thus for every \(i,j\),
\[
\Pr\{\pi_t(i)=j\}=\frac1n+a_n^t\left({\bf1}_{i=j}-\frac1n\right).
\]
Since the diagonal displacement is zero and \(\sum_{i,j}|i-j|=n(n^2-1)/3\), the asserted exact mean follows.

**2. The only second-moment relaxation modes.** Expand \(F(\pi)^2\) into terms \(|\pi(i)-i|\,|\pi(j)-j|\), each depending on at most two specified positions and their assigned values. Therefore \(F^2\), under right translations of \(S_n\), lies in the matrix-coefficient span of the permutation module on ordered pairs of distinct labels, together with the one-point submodule. For \(n\ge4\), the ordered-pair module decomposes as
\[
\mathbf1\oplus2[n-1,1]\oplus[n-2,2]\oplus[n-2,1,1].
\]
The central transition operator is \(P=n^{-1}I+2n^{-2}\sum_{i<j}(ij)\). In an irreducible shape \(\lambda\), its eigenvalue is
\[
\frac1n+\frac{1}{n^2}\sum_{r\ge1}\lambda_r(\lambda_r-2r+1).
\]
These four shapes give the distinct values \(1,a_n,a_n^2,c_n\), respectively. Hence, for constants \(A_n,B_n,C_n\),
\[
\mathbb E F_t^2=m_n^2+v_n+A_na_n^t+B_na_n^{2t}+C_nc_n^t.
\]
This holds for all integer \(t\ge0\), and does not assume that finite numerical enumeration determines the spectrum.

**3. Determine the four constants exactly.** Under the uniform permutation law, let \(r_i=\sum_j|i-j|=i(i-1)/2+(n-i)(n-i+1)/2\). Direct summation gives
\[
\sum_{i,j}|i-j|^2=\frac{n^2(n^2-1)}6,\qquad
\sum_i r_i^2=\frac{n(n^2-1)(7n^2-8)}{60}.
\]
The two-card uniform-permutation formula
\[
\mathbb E_{\rm unif} F^2=\frac1n\sum_{i,j}|i-j|^2+
\frac{(\sum_{i,j}|i-j|)^2-2\sum_i r_i^2+\sum_{i,j}|i-j|^2}{n(n-1)}
\]
gives \(\operatorname{Var}_{\rm unif} F=v_n\).

At time zero, \(\mathbb EF_0^2=0\). A single nontrivial transposition of positions \(i<j\) has squared footrule \(4(j-i)^2\) and probability \(2/n^2\), so
\[
\mathbb EF_1^2=\frac{2(n^2-1)}3.
\]
For two steps, the events with exactly one identity selection contribute \((2/n)\mathbb EF_1^2\). Equal nontrivial transpositions cancel. Two distinct transpositions sharing a vertex of a triple \(i<j<k\) yield a three-cycle with squared footrule \(4(k-i)^2\), and there are six ordered pairs of such edges. Two disjoint transpositions on \(i<j<k<\ell\) give three perfect matchings, each in two orders. Their complete squared-footrule sums are
\[
\begin{aligned}
T_3&=\sum_{i<j<k}24(k-i)^2
=\frac{2n(n-2)(n-1)(n+1)(3n+1)}5,\\
T_4&=\sum_{i<j<k<\ell}8\left[((j-i)+(\ell-k))^2+2((k-i)+(\ell-j))^2\right]\\
&=\frac{n(n-3)(n-2)(n-1)(n+1)(25n+8)}{45}.
\end{aligned}
\]
These evaluations follow by summing arithmetic progressions and powers of the integer gaps; no finite cutoff is used. Therefore
\[
\begin{aligned}
\mathbb E F_2^2
&=\frac2n\mathbb E F_1^2+\frac4{n^4}(T_3+T_4)\\
&=\frac{4(n-1)(n+1)(25n^3-48n^2+20n+12)}{45n^3}.
\end{aligned}
\]
Solving the three resulting linear equations using the distinct modes gives
\[
\begin{aligned}
A_n&=-\frac{2(n^2-1)(5n^2-2n-9)}{45},\\
B_n&=\frac{n(n-3)(n+1)(7n+2)}{90},\\
C_n&=\frac{(n^2-1)(n^2-4)}{30}.
\end{aligned}
\]
Finally subtract \((\mathbb EF_t)^2=m_n^2(1-2a_n^t+a_n^{2t})\), yielding the displayed variance identity.

**4. Strict finite-deck overshoot.** Write the variance difference as \(K_na_n^t+L_na_n^{2t}+C_nc_n^t\), with \(K_n=4(n^2-1)(n+2)/45>0\). For \(n\ge4\), \(0\le c_n<a_n<1\) and \(a_n^2<a_n\). Consequently the positive \(K_na_n^t\) term dominates as \(t\to\infty\); the variance eventually exceeds \(v_n\). At \(t=0\) the variance is zero, so nonmonotonicity is unavoidable.

**5. Large-deck crossover and maximizer.** For fixed \(s\), \(a_n^{t_n}\to e^{-s}\) and \(c_n^{t_n}\to e^{-2s}\). The coefficients of \(a_n^{2t}\) and \(c_n^t\) individually have leading order \(n^4\); their cancellation requires one further order. The exact identity
\[
\frac{c_n}{a_n^2}=1-\frac4{(n-2)^2}
\]
gives
\[
c_n^{t_n}-a_n^{2t_n}=-\frac{2s}{n}e^{-2s}+O_s(n^{-2}).
\]
Inserting this in the variance formula and collecting all terms of order \(n^3\) yields \(V(s)\). Direct differentiation gives
\[
V'(s)=\frac{e^{-2s}}{45}\bigl(9+6s-4e^s\bigr).
\]
The function \(4e^s-9-6s\) is negative at zero, first decreases, then increases strictly to infinity; it has exactly one positive zero. Therefore \(V\) has exactly one global maximum. Evaluating its unique defining equation yields the displayed constants. This proves the claimed finite-time variance overshoot and limiting optimization.

## Verification

The included standard-library-only `verify_footrule.py` enumerates complete discrete-time transition distributions for \(n=4,5,6\) through time \(t=5\) using exact rational arithmetic, checks both mean and variance formulas, checks the triple and quadruple combinatorial sums for all \(4\le n\le12\), and evaluates the asymptotic crossover numerically. It passed 59 assertions on the reviewed package. Separately, symbolic algebra verifies the identities at \(t=0,1,2\) and the uniform-permutation second-moment formula. These computations are independent consistency checks on explicit formulas; the proof of all \(n\) and \(t\) rests on the spectral decomposition and finite combinatorial sums, not on finite experiments.

To reproduce, run `python3 verify_footrule.py` from the directory containing this file and the checker.

## Relationship to prior work

He, Hutsalyuk, Mussardo and Stampiggi (arXiv:2609.13387, first publicly available 11 September 2026) formulate classical random-transposition equilibration as the benchmark for quantum stochastic walks, study global mixing and quantum spectral diagnostics, and provide the model used here; they do not derive this footrule-noise law. Jain and Sawhney (arXiv:2410.23944, first submitted 31 October 2024) analyze sharp total-variation and hitting-time mixing of precisely the same lazy discrete-time chain, not time-dependent Spearman-footrule variance. Xia, Guan and Xu (arXiv:2505.01825, first submitted 3 May 2025) provide the stationary footrule normalization and null-distribution asymptotics under uniform permutations; the stationary variance \(v_n\) is credited as prior work. The new contribution is the exact **transient variance and its strict/nonmonotone, universal peak**. These established results do not themselves imply the explicit time-dependent covariance coefficients. Standard symmetric-group character theory supplies the spectral framework, not by itself the evaluated footrule projection coefficients.

## Limitations

The result concerns only the classical lazy independent-index random-transposition walk started at identity; it does not prove a quantum mixing speedup or transfer its variance law to the quantum stochastic model. The asymptotic time is \(O(n)\), not the total-variation cutoff window. The convergence theorem is pointwise in fixed \(s\), and the continuous limiting curve's maximizer does not, by itself, prove convergence of every finite-deck global maximizer without uniform tail bounds. The originality assessment is based on accessible, materially inspected primary literature and available research records; broad representation-theoretic formula collections or unlocated observable-specific work might already contain an equivalent expansion. No independent proof audit or publication-priority audit has occurred.

## References

1. F. He, A. Hutsalyuk, G. Mussardo and A. Stampiggi, *Quantum Stochastic Walks on the Permutation Group*, arXiv:2609.13387 (first submitted 2026-09-11), https://arxiv.org/abs/2609.13387.
2. V. Jain and M. Sawhney, *Hitting time mixing for the random transposition walk*, arXiv:2410.23944 (first submitted 2024-10-31), https://arxiv.org/abs/2410.23944.
3. L. Xia, L. Guan and W. Xu, *Asymptotic representations for Spearman's footrule correlation coefficient*, arXiv:2505.01825 (first submitted 2025-05-03), https://arxiv.org/abs/2505.01825.
4. P. Diaconis and M. Shahshahani, *Generating a random permutation with random transpositions*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981), 159–179.
5. P. Diaconis and R. L. Graham, *Spearman's footrule as a measure of disarray*, J. Royal Statist. Soc. Ser. B 39 (1977), 262–268.
