# Universality of scalar asymptotic-expansivity phase diagrams for normal dynamics

## Finding

**Realization theorem.** Let \(K\subset[1,2]\) be any nonempty compact set, and let \(A\subseteq K\) be any at most countable set containing every isolated point of \(K\). There is a bounded, positive, invertible, self-adjoint operator \(T\) on a separable nonzero complex Hilbert space with \(\sigma(T)=K\) and the following *simultaneous* scalar phase diagram. Write
\[
J_K=\{r\in K:\exists\delta>0\text{ with }K\cap(r-\delta,r)=\varnothing\}.
\]
For every nonzero complex scalar \(c\), put \(r=1/|c|\). Then
\[
\begin{aligned}
cT\text{ is not asymptotically expansive} &\iff r\in A,\\
cT\text{ is not strongly asymptotically expansive} &\iff r\in (K\setminus J_K)\cup A,\\
cT\text{ is not hyperbolic} &\iff r\in K.
\end{aligned}
\]
Conversely, *every* positive self-adjoint operator on a separable complex Hilbert space with nonempty spectrum in \([1,2]\) yields a pair \((K,A)\) satisfying precisely these conditions, so they classify all realizable triples of radial failure sets in this class. The spectral implications for a fixed normal operator are previously known; **the contribution here is the complete realization of every admissible pair and its induced three-property phase diagram**, rather than another fixed-operator criterion.

**Dense interleaving example.** Take \(K=1+C\), where \(C\) is the usual middle-third Cantor set, and \(A=\varnothing\). Every \(cT\) is asymptotically expansive. Among the scalars for which \(cT\) is not hyperbolic, strong asymptotic expansivity holds precisely at reciprocals of the minimum and right endpoints of complementary Cantor gaps; strong asymptotic expansivity fails at reciprocals of the remaining Cantor points. Both subsets are dense in the reciprocal Cantor set.

## Assumptions and scope

The Hilbert space is complex and nonzero, separable for the realization/classification assertion. An operator \(S\) is **asymptotically expansive** (AE) if there exists \(\delta>0\) such that \(\sup_{n\ge0}\|S^nx\|\le\delta\) implies \(\|S^nx\|\to0\). It is **strongly asymptotically expansive** (SAE) if, in addition, for this \(\delta\) the convergence is uniform over all such \(x\). It is **hyperbolic** if its spectrum misses the unit circle. Zero scalar multiples possess all three properties. These are the conventions of Bag, Mandal and Das (2026).

For a general bounded normal operator, the same radial formula applies with \(K=\sigma(|T|)\cap(0,\infty)\) and \(A=\{r>0:E_{|T|}(\{r\})\ne0\}\), including when zero belongs to the modulus spectrum. A point belongs to \(J_K\) if it has a spectral gap immediately to its left. Its spectral gap need not extend to the right. Points isolated in \(K\) necessarily belong to \(A\) when \(K\) is the support of a projection-valued spectral measure on a nonzero Hilbert space.

## Proof

**1. Radial spectral reduction (known fixed-operator criterion).** Let \(T\) be bounded normal, \(B=|T|\), and let \(E\) be the spectral resolution of \(B\). For a nonzero scalar \(c\), let \(r=1/|c|\). For every \(x\) and integer \(n\ge0\), the spectral theorem gives
\[
\|(cT)^n x\|^2=\int_{[0,\|T\|]}(t/r)^{2n}\,d\langle E(t)x,x\rangle.
\]
By monotone convergence on the part \(t>r\), an orbit is bounded exactly when \(x\in E([0,r])H\). On this subspace, dominated convergence yields
\[
\lim_{n\to\infty}\|(cT)^n x\|^2=\|E(\{r\})x\|^2.
\]
Scaling bounded vectors shows AE is equivalent to \(E(\{r\})=0\). For SAE, all vectors with norm at most \(\delta\) in the reducing subspace \(E([0,r])H\) automatically have all orbit norms at most \(\delta\). Therefore SAE is equivalent to the operator-norm convergence \(\|(cT)^n E([0,r])\|\to0\). If \(r\in A\), this fails on an eigenvector; if \(r\in K\setminus J_K\), every interval \((r-\epsilon,r)\) carries a nonzero spectral projection, so the norm of the restricted iterate is \(1\) for every \(n\). If \(r\notin K\), or \(r\in J_K\setminus A\), the part of the spectrum on \([0,r]\) is bounded by some \(r-\epsilon\), and the restricted powers decay geometrically. Thus SAE fails exactly on \((K\setminus J_K)\cup A\). Finally, normal spectral mapping gives \(\{|z|:z\in\sigma(T)\}=\sigma(|T|)\), hence hyperbolicity fails precisely for \(r\in K\). All steps hold whether \(E([0,r])H\) is zero or not.

**2. Necessity of the pair constraints.** Eigenprojections at distinct positive radii have orthogonal nonzero ranges; separability makes their set of radii at most countable. If \(r\) is isolated in \(K=\sigma(T)\), the spectral projection of an open interval meeting \(K\) only at \(r\) cannot be zero (otherwise \(r\) is outside the operator spectrum), so \(r\in A\). Necessity follows.

**3. Existence of every admissible pair.** Let \(I\) be the isolated points of \(K\). The Cantor–Bendixson theorem supplies a closed perfect kernel \(P\subseteq K\) whose complement is countable. Moreover \(K=\overline{P\cup I}\): otherwise a nonempty relatively open set in \(K\) would be disjoint from both \(P\) and \(I\); it would be countable and have no isolated point, contradicting the perfect-set property of countable locally compact metric spaces (or the Cantor–Bendixson theorem applied inside a smaller compact neighborhood). Thus \(K=\overline{P\cup A}\), since \(I\subseteq A\).

If \(P\ne\varnothing\), choose a nonatomic Borel probability measure \(\nu\) with support \(P\). For completeness, take a countable relative-open base of \(P\), place a nonatomic Cantor probability supported on a compact perfect subset of each nonempty basis member, and add them with positive summable weights. If \(A\) is enumerated without repetition as \(\{a_j\}\), put
\[
\mu=\frac{\mathbf1_{P\ne\varnothing}\nu+\sum_j2^{-j}\delta_{a_j}}{\mathbf1_{P\ne\varnothing}+\sum_j2^{-j}}.
\]
At least one numerator term is nonzero. This is a finite positive Borel probability, supported exactly on \(K\), whose atoms occur precisely at the points of \(A\). On \(H=L^2(K,\mu)\), define \((Tf)(t)=t f(t)\). Then \(T\) is positive, self-adjoint and boundedly invertible, \(\sigma(T)=\operatorname{supp}\mu=K\), and \(E(\{r\})\ne0\iff\mu(\{r\})>0\iff r\in A\). Apply Step 1 to obtain every claimed phase diagram. This construction also covers \(A=\varnothing\), all-perfect \(K\), purely countable \(K\), and singleton \(K\).

**4. Cantor separation.** For \(K=1+C\), there are no isolated points and the standard nonatomic Cantor measure gives \(A=\varnothing\). The left-isolated points of \(K\) are its minimum and the right endpoints of complementary middle-third intervals. Such right endpoints form a countable dense subset; the complement of that subset in \(K\) is also dense (\(C\) has no isolated points). The claimed simultaneous dense SAE/non-SAE behavior follows. In the reciprocal scalar coordinate, continuous inversion preserves relative denseness.

## Verification

The analytic checks are the spectral integral, the uniform-norm characterization, the Cantor–Bendixson density argument, and the nonatomic-plus-atomic realization. The checked boundary cases are isolated spectral points, a spectral minimum with no atom, left gap endpoints with no atom, and continuous spectral accumulation from below. The supplied optional checker reproduces elementary exact rational finite-level Cantor-gap identities; its finite tests do not establish the infinite realization theorem. Reproduce with `python3 check.py` from the extracted package directory. No external dependency is required.

## Relationship to prior work

Bag–Mandal–Das introduced AE and SAE and explicitly asked for scalar-multiple failure sets in their October 2026 work. Earlier normal-operator criteria for one fixed operator, including a previously recorded normal spectral classification, already imply the formulas in Step 1; this work does not claim those formulas as novel. Classical stability of normal contractions, as described in the 2024 operator stability literature, also implies the strong-convergence portion. The additional statement that **every and only** admissible compact-spectrum/countable-atom pair can occur, yielding the complete set of possible scalar AE/SAE/hyperbolicity diagrams, is the proposed new classification. The Cantor example exhibits dense opposing strong-expansivity behavior inside one fixed nonhyperbolic radial spectrum; it is not inferred just from naming an isolated example in the earlier literature.

## Limitations

The realization theorem requires separability and compact positive radial spectra in \([1,2]\), rather than arbitrary Banach operators or prescribed complex spectral phases. It does not classify nonnormal scalar dynamical phase diagrams. The first spectral characterization is antecedent mathematics, not a new result. The perfect-set and spectral-theorem arguments are mathematical proofs; exact finite checks cannot substitute for them. Priority remains conditional on literature not inspected or indexed, and no independent external assessment has been conducted.

## References

1. P. Bag, P. N. Mandal and P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1 (first public October 1, 2026). https://arxiv.org/html/2610.01196v1
2. *Convergence of power sequences of operators via their stability*, *Banach Journal of Mathematical Analysis* (2024), DOI:10.1007/s43037-024-00371-9. https://link.springer.com/article/10.1007/s43037-024-00371-9
3. Cantor–Bendixson perfect-set theorem (classical); normal-operator spectral theorem (classical).
