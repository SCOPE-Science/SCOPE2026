# Uniform cyclic-incidence one-type spectra and a sharp algebraic growth law

## Finding
Fix integers \(r\ge1\) and \(n\ge2r+1\). Let \(P_{n,r}\) be the height-two poset of \(2n\) individually named elements \(a_i,b_j\), for \(i,j\in\mathbb Z/n\mathbb Z\), whose only strict relations are \(a_i<b_j\) when \(j-i\pmod n\in\{0,\ldots,r-1\}\). Embed it in the countable universal homogeneous poset \(\mathbb D\). For a nonalgebraic complete one-type of a new point \(x\), let \(L=\{p\in P_{n,r}:p<x\}\) and \(U=\{p\in P_{n,r}:x<p\}\). Let \(M_{n,r}(u,v)\) count the types having both \(L\) and \(U\) nonempty, with weight \(u^{|L|}v^{|U|}\). Then
\[
\boxed{M_{n,r}(u,v)=n\left[u((1+v)^r-1)+u^2\sum_{s=1}^{r-1}(1+u)^{s-1}((1+v)^{r-s}-1)\right].}
\]
In particular, exactly \(nr2^{r-1}\) nonalgebraic types put \(x\) strictly between named points.

Define the integer \(r\times r\) matrix \(T_r\), with indices \(0,\ldots,r-1\), by adding \(1\) in entry \((i,0)\) and adding \(1\) in entry \((i,i+1)\) for \(i<r-1\), or \(2\) in entry \((r-1,r-1)\) for \(i=r-1\). (Contributions are added if entries coincide, as when \(r=1\).) The number \(t_{n,r}\) of all nonalgebraic one-types is
\[
\boxed{t_{n,r}=2\operatorname{tr}(T_r^n)+nr2^{r-1}-1.}
\]
Moreover,
\[
\boxed{\det(\lambda I-T_r)=\lambda^r-3\lambda^{r-1}+\sum_{j=0}^{r-2}\lambda^j
=\frac{\lambda^{r-1}(\lambda-2)^2-1}{\lambda-1}.}
\]
The apparent quotient singularity at \(\lambda=1\) is removable; the sum is empty for \(r=1\). If \(\rho_r>2\) is the unique solution of \(\rho_r^{r-1}(\rho_r-2)^2=1\), then, for fixed \(r\) as \(n\to\infty\),
\[
\boxed{t_{n,r}\sim2\rho_r^n.}
\]
The growth bases strictly decrease with the incidence width, \(\rho_1>\rho_2>\cdots>2\), and \(\rho_r\downarrow2\). There are exactly \(2n\) additional algebraic equality types.

## Assumptions and scope
The symbols \(a_i,b_j\) denote distinct named parameters, and \(P_{n,r}\) is an induced finite subposet of \(\mathbb D\). Type counts do not quotient by cyclic rotations. All assertions hold for every integer \(r\ge1\) and \(n\ge2r+1\); the lower bound on \(n\) is used for uniqueness of short cyclic spans and is not claimed optimal. A type is nonalgebraic when \(x\) is unequal to every named parameter. The conventions include \(0\times0\) empty sums and the one-state matrix \(T_1=(3)\).

## Proof
**1. Admissible extensions.** Given a finite parameter poset \(P\), choosing a new nonparameter point \(x\) is equivalent to choosing a down-set \(L\subseteq P\), an up-set \(U\subseteq P\), with \(L\cap U=\varnothing\) and \(l<u\) for all \(l\in L,u\in U\). Necessity follows by transitivity; conversely, the declared comparisons define a partial order. The extension property and ultrahomogeneity of \(\mathbb D\) give a unique complete nonalgebraic one-type per pair. If either \(L\) or \(U\) is empty, there are \(2J(P)-1\) choices, where \(J(P)\) is the number of down-sets (up-sets are equinumerous by complementation). If both are nonempty in a height-two poset, every element of \(L\) must be minimal and every element of \(U\) maximal. Consequently two-sided extensions of \(P_{n,r}\) are exactly nonempty pairs \(X\subseteq\{a_i\}\), \(Y\subseteq\{b_j\}\) with every \(a\in X\) below every \(b\in Y\): the nonempty bicliques of its bipartite incidence graph.

**2. A bivariate cyclic biclique count.** For a nonempty \(X\) with a common upper neighbor, all its indices lie in an arc of \(r\) consecutive cyclic positions. Since \(n\ge2r+1\), there is a unique shortest cyclic arc containing \(X\), as long as its span (last minus first index in cyclic order) is \(s\le r-1\). Indeed, its complementary gap has length at least \(n-(r-1)>n/2\), and two distinct gaps of that length cannot occur. Intersecting the \(r\)-consecutive upper-neighbor arcs of elements of \(X\) leaves exactly \(r-s\) common upper neighbors. For \(s=0\), the set \(X\) is a singleton; there are \(n\) such sets, each having \(r\) upper neighbors, giving \(nu((1+v)^r-1)\). For \(1\le s<r\), the first and last positions are required, the \(s-1\) interior lower positions can be chosen independently, and the upper set can be any nonempty subset of the \(r-s\) common neighbors. This gives precisely \(nu^2(1+u)^{s-1}((1+v)^{r-s}-1)\). Summing proves the polynomial identity. In particular its evaluation at \(u=v=1\) is
\[
M_{n,r}(1,1)=n\left[(2^r-1)+\sum_{s=1}^{r-1}2^{s-1}(2^{r-s}-1)\right]=nr2^{r-1}.
\]
All potential bicliques have been included exactly once by their unique lower span.

**3. Cyclic ideal count.** To specify an ideal, first choose its included upper elements \(b_j\), encoded by a binary cyclic word \(z_j\) with \(z_j=1\) when \(b_j\) is included. A lower element \(a_i\) is forced into the ideal if any one of \(b_i,\ldots,b_{i+r-1}\) is included. Otherwise \(a_i\) is optional. Thus
\[
J(P_{n,r})=\sum_{z\in\{0,1\}^n}2^{N_r(z)},\qquad N_r(z)=\#\{i:z_i=\cdots=z_{i+r-1}=0\},
\]
with cyclic indices. Read the word cyclically, maintaining the length of the current trailing zero-run, capped at \(r-1\). Reading a one resets the state to zero and has weight one. Reading a zero increases the state by one unless already capped; when already capped, the new zero completes a window of \(r\) zeros and receives weight two. This is exactly \(T_r\). Every cyclic binary word gives a unique closed state trajectory (the all-zero word stays capped), and any closed trajectory determines its word, with duplicate transitions distinguished by their input labels when \(r=1\). Therefore \(J(P_{n,r})=\operatorname{tr}(T_r^n)\). Combining with Step 1 and Step 2 gives the displayed type formula.

**4. Characteristic polynomial and asymptotics.** Expanding \(\det(\lambda I-T_r)\) along the first column (or eliminating the successive zero-run states) gives
\[
p_r(\lambda)=\lambda^r-3\lambda^{r-1}+\lambda^{r-2}+\cdots+\lambda+1.
\]
Direct multiplication proves \((\lambda-1)p_r(\lambda)=\lambda^{r-1}(\lambda-2)^2-1\), including \(r=1\). The nonnegative matrix \(T_r\) is irreducible (every state reaches zero and zero reaches every state) and aperiodic (state zero has a self-loop). Perron–Frobenius theory supplies a simple strictly dominant positive eigenvalue. Since the function \(f_r(\lambda)=\lambda^{r-1}(\lambda-2)^2\) is strictly increasing on \((2,\infty)\), with range \((0,\infty)\), its unique \(>2\) solution \(\rho_r\) is that eigenvalue. The remaining eigenvalues have strictly smaller modulus, whence \(\operatorname{tr}(T_r^n)=\rho_r^n+o(\rho_r^n)\). The linear mixed term is negligible. Finally \(f_{r+1}(\lambda)=\lambda f_r(\lambda)>f_r(\lambda)\) for \(\lambda>2\), proving \(\rho_{r+1}<\rho_r\). The identity \(\rho_r-2=\rho_r^{-(r-1)/2}\le2^{-(r-1)/2}\) proves \(\rho_r\to2\), completing the proof. \(\square\)

## Verification
The standard-library companion `verify.py` independently enumerates every choice of included lower parameters to count ideals, and every nonempty lower subset with all its common upper neighbors to count two-sided patterns. For each of 18 parameter pairs with \(1\le r\le6\) and \(2r+1\le n\le2r+3\), the enumerated counts agree with \(\operatorname{tr}(T_r^n)\) and \(nr2^{r-1}\). As a separate bivariate test, setting \(u=2,v=3\) in the direct enumeration agrees with the displayed mixed polynomial. Run `python3 verify.py`; the output is supplied in `verification_output.txt`. These finite tests do not replace the all-parameter proof.

## Relationship to prior work
The interpretation of one-point extensions of a finite poset by an ideal, a filter, and their compatibility is standard; Dolinka and Mašulović use it in their work on ultrahomogeneous structures (arXiv:1009.2892). A publicly archived study of finite-parameter one-type counting in the random poset establishes the general complexity of the counting task and the ideal/filter correspondence, but does not evaluate this cyclic family or provide the mixed-type polynomial. Trotter studied dimensions of generalized crowns in 1974, not their finite-parameter type spectra. Munarini studied order ideals of a garland (2005); his paper contains a different specialized recurrence and does not address the present random-poset types. Earlier work of Munarini and Zagaglia Salvi on ordinary crowns covers the two-neighbor ideal-count special case. Munarini's 2006 paper on generalized fences/crowns relates ideal enumeration to Chebyshev polynomials and may overlap the ideal-count component, which is **not** claimed separately as a novelty. The contribution here is the uniform all-width **bivariate two-sided type polynomial**, its combination with the one-sided ideal trace into a complete type spectrum, and the exact algebraic growth-base law and width monotonicity.

## Limitations
The proof concerns fixed finite \(r\) and \(n\ge2r+1\), with individually named parameters. It does not determine smaller-circumference boundary cases or types of arity greater than one. The abstract of Munarini's broader 2006 Chebyshev work was available, but its full text was not inspected; it could contain an equivalent ideal-recurrence or numerical observation. The full text of Trotter's 1974 article was not obtained. A separately established fixed-width three-neighbor enumeration is a special case of the new uniform statement and is not passed off as independent. Searches cannot exclude an equivalent biclique polynomial or exact type law in unindexed combinatorial literature. No independent scientific audit has been performed.

## References
1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, first submitted 15 September 2010; Proceedings of the Edinburgh Mathematical Society 55 (2012), 635–656. https://arxiv.org/abs/1009.2892
2. W. T. Trotter Jr., *Dimension of the crown \(S_n^k\)*, Discrete Mathematics 8 (1974), 85–103. https://doi.org/10.1016/0012-365X(74)90113-7
3. E. Munarini, *Enumeration of Order Ideals of a Garland*, Ars Combinatoria 76 (2005), 185–192. https://combinatorialpress.com/ars-articles/volume-076-ars-articles/enumeration-of-order-ideals-of-a-garland/
4. E. Munarini and N. Zagaglia Salvi, *On the rank polynomial of the lattice of order ideals of fences and crowns*, Discrete Mathematics 259 (2002), 163–177. https://doi.org/10.1016/S0012-365X(02)00378-3
5. E. Munarini, *A Combinatorial Interpretation of the Chebyshev Polynomials*, SIAM Journal on Discrete Mathematics 20 (2006), 649–655. https://doi.org/10.1137/S0895480103432283
6. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly archived mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1
