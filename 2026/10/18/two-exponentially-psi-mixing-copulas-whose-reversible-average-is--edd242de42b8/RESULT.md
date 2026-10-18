# Two exponentially \(\psi\)-mixing copulas whose reversible average is never \(\psi\)-mixing

## Finding
There exist two bivariate copulas \(C\) and \(C^{\mathrm T}\), each generating an exponentially \(\psi\)-mixing stationary Markov chain with uniform marginals, such that their equal-weight mixture \(\overline C=(C+C^{\mathrm T})/2\) generates a **reversible, uniformly geometrically ergodic** stationary Markov chain satisfying
\[
\psi_n(\overline C)=\infty\quad\text{for every integer }n\ge1.
\]
In fact, each component obeys the exact coefficient law
\[
\psi_n(C)=\psi_n(C^{\mathrm T})=2^{2-n}\quad(n\ge2),
\]
while the mixture has an explicit three-step minorization
\[
\overline P^{\,3}(x,A)\ge \frac3{32}\,\mu(A)\quad\text{for every }x\in[0,1),\;A\text{ measurable},
\]
where \(\mu\) denotes Lebesgue probability measure on \([0,1)\). Thus exponentially \(\psi\)-mixing copula generators are **not** closed under convex combinations, even when the convex combination is time-reversal symmetrization and remains rapidly mixing in total variation.

## Assumptions and scope
Let \(I_0=[0,1/3)\), \(I_1=[1/3,2/3)\), \(I_2=[2/3,1)\). Let \(U_j\) be uniform probability measure on \(I_j\). Define the Markov transition kernel \(P\), for every \(x\in[0,1)\), by
\[
P(x,\mathrm dy)=
\begin{cases}
\delta_{x+1/3}(\mathrm dy), &x\in I_0,\\
\tfrac12 U_0(\mathrm dy)+\tfrac12 U_2(\mathrm dy),&x\in I_1\cup I_2.
\end{cases}
\]
Define its reverse kernel \(R\) by
\[
R(x,\mathrm dy)=
\begin{cases}
\delta_{x-1/3}(\mathrm dy),&x\in I_1,\\
\tfrac12 U_1(\mathrm dy)+\tfrac12 U_2(\mathrm dy),&x\in I_0\cup I_2.
\end{cases}
\]
Use \(P\), \(R\) and \(Q=(P+R)/2\) with the common stationary law \(\mu\). The one-step bivariate copula corresponding to a kernel \(K\) is the distribution of \((X_0,X_1)\) under \(X_0\sim\mu\) and \(X_1\mid X_0=x\sim K(x,\cdot)\). These are legitimate copulas because both coordinates are uniform. Only one-dimensional Lebesgue state space and stationary chains are asserted, not absolutely continuous one-step copulas.

For a stationary Markov kernel \(K\) with invariant \(\mu\), use the standard coefficient
\[
\psi_n(K)=\sup_{\substack{A,B\subseteq[0,1)\text{ measurable}\\\mu(A)\mu(B)>0}}
\left|\frac{\int_A K^n(x,B)\,\mu(\mathrm dx)}{\mu(A)\mu(B)}-1\right|.
\]
This equals the usual stationary full-past/future \(\psi\)-mixing coefficient at lag \(n\) by the Markov property: conditional probabilities of future events are bounded functions of the state at the beginning of the future block, and conditioning on the entire past only changes the distribution of its latest state. Finite coefficients at the first few lags are **not** required for \(\psi\)-mixing; convergence to zero is.

## Proof
**1. Uniform stationarity and reversal.** On the three partition cells the transition matrix of \(P\) is
\[
M=\begin{pmatrix}0&1&0\\\tfrac12&0&\tfrac12\\\tfrac12&0&\tfrac12\end{pmatrix}.
\]
Every row and every column sums to one, so the equal-mass three-cell law is stationary. More specifically, the first rule maps \(\mu\) restricted to \(I_0\) measure-preservingly onto \(I_1\), while the other two rules send their mass uniformly into \(I_0\) and \(I_2\). Consequently \(P\) preserves the *full* Lebesgue law, not merely cell masses. Reversing its stationary joint measure gives exactly \(R\) as defined above: \(R\) has cell transition matrix \(M^{\mathrm T}\). Both copulas have uniform margins; they are transposes of each other. Their average \(Q\) is self-adjoint with respect to \(\mu\), hence reversible.

**2. Exact exponential \(\psi\)-mixing of both components.** In every two-step path of \(P\), at least one of the two transitions is a fresh uniform draw, so all dependence on the precise starting point inside its cell is erased by time two. Therefore, for every \(n\ge2\), \(x\in I_i\), and measurable \(A\),
\[
P^n(x,A)=\sum_{j=0}^2 (M^n)_{ij}U_j(A).
\]
Direct multiplication yields
\[
M^2=\begin{pmatrix}\tfrac12&0&\tfrac12\\\tfrac14&\tfrac12&\tfrac14\\\tfrac14&\tfrac12&\tfrac14\end{pmatrix},\qquad
M^3=\begin{pmatrix}\tfrac14&\tfrac12&\tfrac14\\\tfrac38&\tfrac14&\tfrac38\\\tfrac38&\tfrac14&\tfrac38\end{pmatrix}.
\]
Let \(J\) denote the three-by-three matrix all of whose entries are \(1/3\). Matrix multiplication gives \(MJ=J\) and
\[
M(M^2-J)=-\tfrac12(M^2-J).
\]
Hence, by induction, for every \(n\ge2\),
\[
M^n=J+(-\tfrac12)^{n-2}(M^2-J).
\]
The \(n\)-step transition density with respect to \(\mu\) is constant on each \(I_i\times I_j\) and equals \(3(M^n)_{ij}\). Therefore
\[
\psi_n(P)=\max_{i,j}|3(M^n)_{ij}-1|
=2^{2-n}\quad(n\ge2).
\]
The maximum is *attained* by choosing partition cells \(A=I_i\) and \(B=I_j\) where the displayed maximum occurs, because the densities are block-constant. Since \(R\) is the stationary reversal, its \(n\)-step block matrix is \((M^n)^{\mathrm T}\) and it has the same exact coefficient. This proves exponential \(\psi\)-mixing of the two components.

**3. Singular alternating branch in every mixture power.** Expand \(Q^n\) as the equal-weight mixture of the \(2^n\) kernel compositions from \(\{P,R\}\). Choose the word that alternates \(P,R,P,R,\ldots\), starting with \(P\); its weight is \(2^{-n}\). For each \(x\in I_0\), every transition along this word is deterministic: \(P\) sends \(x\) to \(x+1/3\in I_1\), while \(R\) returns that point to \(x\). Thus the chosen word sends \(x\) to \(x\) if \(n\) is even and to \(x+1/3\) if \(n\) is odd.

Fix \(0<\varepsilon<1/3\), let \(A=[0,\varepsilon)\), and take \(B=A\) for even \(n\) or \(B=A+1/3\) for odd \(n\). Since all other word contributions are nonnegative,
\[
\Pr_Q(X_0\in A,X_n\in B)\ge 2^{-n}\varepsilon,
\qquad\mu(A)=\mu(B)=\varepsilon.
\]
The joint-to-product ratio is therefore at least \(2^{-n}/\varepsilon\). For any fixed \(n\), this tends to infinity as \(\varepsilon\downarrow0\), implying \(\psi_n(Q)=\infty\), even though the singular deterministic branch has exponentially vanishing mass.

**4. Uniform geometric ergodicity survives.** All entries of \(M^3\) are at least \(1/4\). Thus the three-step transition measure of \(P\) satisfies \(P^3(x,A)\ge(3/4)\mu(A)\) for every \(x,A\). The all-\(P\) word of length three occurs in \(Q^3\) with probability \(1/8\), so
\[
Q^3(x,A)\ge \tfrac18P^3(x,A)\ge\tfrac3{32}\mu(A).
\]
Standard splitting of this minorization writes \(Q^3=(3/32)\Pi+(29/32)H\), where \(\Pi(x,\cdot)=\mu\) and \(H\) is a stationary Markov kernel. Iterating yields
\[
\sup_x\|Q^{3k}(x,\cdot)-\mu\|_{\mathrm{TV}}\le(29/32)^k.
\]
This proves uniform geometric ergodicity and, for the stationary Markov chain, exponential decay of strong/absolute-regularity mixing coefficients. It cannot imply \(\psi\)-mixing, whose normalization by arbitrarily small event probabilities detects the singular branch. \(\square\)

## Verification
The self-contained Python 3 script `verify.py` performs exact-rational checks of stationarity, time reversal, all displayed matrix powers, the rank-one recurrence, the two component coefficient profiles through lag 64, and the minorization constant. Its successful run reported **445 checked finite cases** and the exact minorization **\(3/32\)**. These finite checks corroborate algebra; the conclusions for all lags follow from the above induction and singular-branch inequalities, not from numerical extrapolation. Run `python3 verify.py` in a directory containing the extracted file.

## Relationship to prior work
Longla, Mous-Abou and Ngongo [1], Theorem 2.2.2, prove a positive convex-closure theorem under the additional hypothesis \(\psi_1<1\) for every constituent; Section 5 explicitly asks whether closure holds without that restriction. Here the one-step components have singular branches and infinite \(\psi_1\), though their \(\psi_n\) tend to zero exponentially, so that theorem does not apply. Their negative example involving an independence copula and an extremal copula starts from at least one *non*\(\psi\)-mixing constituent; by contrast **both constituents here are exponentially \(\psi\)-mixing**. The 2024 sufficient criterion of Longla [2] requires an iterated density of the mixture to be bounded (or a related full-density bound); the persistent singular component shown here precludes that hypothesis. The 2015 lower-\(\psi\) mixture theorem [3] gives weaker mixing properties. The broad closure assertion in [4], Theorem 2.3.3, is explicitly identified in [1] as lacking a complete proof: its proof incorrectly treats eventual \(\psi\)-mixing as implying a finite one-step coefficient. The example here provides a direct counterexample to that unsupported unrestricted assertion. The present result is a negative answer, by explicit copula kernels, to the general closure question recorded in [1], not an assertion that all convex combinations fail.

## Limitations
The counterexample employs one-step **singular** copulas; it does not address convex closure within subclasses whose kernels have bounded densities at a common iterate. Its one-step coefficients are infinite, although the chains are exponentially \(\psi\)-mixing from lag two onward. It gives one reversible equal-weight mixture of two time-reversed components and does not classify other mixture weights or all possible copulas. The literature comparison is based on the identified primary sources and searchable records; historical priority is not independently certified.

## References
1. M. Longla, H. Mous-Abou and I. S. Ngongo, *On some mixing properties of copula-based Markov chains*, arXiv:2111.14682v1 (first posted 2021-11-29); *Journal of Statistical Theory and Applications* 21 (2022), 131–154, DOI: 10.1007/s44199-022-00045-1. Theorem 2.2.2 and the Section 5 open question.
2. M. Longla, *New copula families and mixing properties*, arXiv:2308.11074v1 (2023-08-21); *Statistical Papers* 65 (2024), 4331–4363, DOI: 10.1007/s00362-024-01559-9. Theorem 3.1 and Corollary 1.
3. M. Longla, *On mixtures of copulas and mixing coefficients*, *Journal of Multivariate Analysis* 139 (2015), 259–265, DOI: 10.1016/j.jmva.2015.03.009.
4. M. Longla, F. D. Ndikwa, M. N. Muia and P. S. Takam, *Perturbations of copulas and mixing properties*, arXiv:2101.04573v1 (first posted 2021-01-12); *Journal of the Korean Statistical Society* 51 (2022), 149–171, DOI: 10.1007/s42952-021-00133-5. Theorem 2.3.3 states broad closure; the 2022 reference [1] explicitly notes that its proof is incomplete.
