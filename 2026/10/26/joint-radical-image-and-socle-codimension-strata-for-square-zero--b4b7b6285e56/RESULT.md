# Joint radical-image and socle-codimension strata for square-zero local algebras

## Finding
Let \(k\) be any field, let \(n\ge 0\), and let \(\ell\ge 1\). Consider ordered \(\ell\)-tuples \((A_1,\ldots,A_\ell)\) of endomorphisms of \(V=k^n\) satisfying \(A_iA_j=0\) for every ordered pair of indices. Set
\[
  a=\dim_k\sum_{i=1}^{\ell}\operatorname{im}A_i,\qquad
  b=\operatorname{codim}_k\bigcap_{i=1}^{\ell}\ker A_i.
\]
These are respectively the dimension of the module radical and the codimension of the module socle for the square-zero local algebra \(k\langle x_1,\ldots,x_\ell\rangle/(x_ix_j:1\le i,j\le\ell)\).

The stratum with prescribed \((a,b)\) is nonempty over every field exactly when either \((a,b)=(0,0)\), or
\[
 a,b\ge 1,\qquad a+b\le n,\qquad a\le\ell b,\qquad b\le\ell a.
\]
Every nonempty stratum is a smooth, geometrically integral, rational, locally closed variety of dimension
\[
 d_{n,\ell}(a,b)=(a+b)n-a^2-b^2+(\ell-1)ab.
\]
Here the assertions concern the natural reduced rank strata; reducedness of the entire defining representation scheme is **not** asserted.

If \(k=\mathbb F_q\), with \(q\) any prime power, the exact number of ordered tuples on that stratum is
\[
 Q_{n,\ell}(a,b;q)= {n\brack a}_q{n-a\brack b}_q H_\ell(a,b;q),
\]
where \({m\brack r}_q\) is the Gaussian binomial coefficient and
\[
 H_\ell(a,b;q)=\sum_{i=0}^{a}\sum_{j=0}^{b}
 {a\brack i}_q{b\brack j}_q(-1)^{a-i+j}
 q^{\binom{a-i}{2}+\binom{j}{2}+\ell i(b-j)}.
\]
In particular \(H_\ell(0,0;q)=1\), and \(Q_{n,\ell}(a,b;q)=0\) outside the stated feasible region. Summing \(Q_{n,\ell}(a,b;q)\) over \((a,b)\) gives the total number of representations of dimension \(n\). The distribution is symmetric in \(a,b\), by simultaneous transposition of all matrices.

## Assumptions and scope
The field is arbitrary for the geometric and nonemptiness statements and a finite field for the cardinality formula. The tuple is labeled and ordered, and each of the \(\ell^2\) products, including squares, must vanish. The integer \(n\) may be zero; the unique zero-dimensional representation has \((a,b)=(0,0)\). No quotient by change of basis is taken. The stated geometric strata are reduced locally closed subvarieties of the matrix tuple space, not assertions about the entire possibly nonreduced representation scheme.

## Proof
**1. Canonical flag.** Set \(W=\sum_i\operatorname{im}A_i\) and \(K=\bigcap_i\ker A_i\). The relations give \(W\subseteq K\). The dimensions are \(\dim W=a\) and \(\dim(V/K)=b\). Conversely, fixing a flag \(W\subseteq K\subseteq V\) with these dimensions, every compatible tuple is uniquely a family of \(\ell\) maps \(T_i:V/K\to W\). Such a tuple has precisely the prescribed flag if and only if the \(T_i\) have joint image spanning \(W\) and joint kernel zero. Thus the rank stratum is the open set of joint-surjective and joint-injective \(\ell\)-families in the rank-\(\ell ab\) Hom vector bundle over the two-step partial flag variety.

**2. Feasibility and geometry.** The joint image has dimension at most \(\ell b\), and injectivity of the stacked map from \(V/K\) into \(W^\ell\) requires \(b\le\ell a\); also \(a+b\le n\). If \(a\ge b\), make the first map injective onto the first \(b\) chosen basis vectors of \(W\) and use distinct positions among the remaining \((\ell-1)b\) source-coordinate slots to reach every remaining basis vector of \(W\). The stacked map stays injective. If \(b\ge a\), make the first map surjective using the first \(a\) input basis vectors and use the remaining \(\ell-1\) maps to send the other \(b-a\) input basis vectors to distinct output-coordinate slots. The stacked map is then injective. These constructions work over every field. For \(a=b=0\), only the zero tuple occurs; exactly one of \(a,b\) being zero is impossible. The partial flag variety is smooth, geometrically integral, and rational, and the nonempty open subset of its Hom bundle inherits those properties. The flag has dimension \(a(n-a)+b(n-a-b)\); adding \(\ell ab\) yields the displayed dimension.

**3. Finite-field count.** There are \({n\brack a}_q\) choices of \(W\), and \({n-a\brack b}_q\) choices of the codimension-\(b\) subspace \(K\) containing it. For fixed \(W\) and \(K\), let \(E=V/K\), with \(\dim E=b\). The Möbius function of the lattice of subspaces satisfies \(\mu(U,W)=(-1)^{a-\dim U}q^{\binom{a-\dim U}{2}}\) and \(\mu(0,T)=(-1)^{\dim T}q^{\binom{\dim T}{2}}\). By Möbius inversion on target-image containment and common-kernel containment, the number of \(\ell\)-families \(E\to W\) with full joint image and trivial joint kernel is
\[
 \sum_{U\le W}\sum_{T\le E}\mu(U,W)\mu(0,T)
 q^{\ell\dim U(\dim E-\dim T)}.
\]
The exponent counts all \(\ell\)-families of maps \(E/T\to U\). Grouping subspaces by dimensions \(i=\dim U\) and \(j=\dim T\) gives \(H_\ell(a,b;q)\). Multiplying by the flag count proves the theorem. Simultaneous transposition interchanges joint image dimension and common-kernel codimension, proving \(Q_{n,\ell}(a,b;q)=Q_{n,\ell}(b,a;q)\).

## Verification
The accompanying Python 3 program `loewy_rank_verify.py` enumerates finite-field matrices, checks every ordered square-zero and mutually annihilating tuple for eight independently selected cases, computes both matrix ranks directly, and compares the complete distribution with the Gaussian/Möbius formula. Checks include the nonprime field \(\mathbb F_4\). It reports `VERIFY_OK_LOEWY_RANK_STRATA_ALL_CASES`. In particular, for two operators on a three-space, the verified totals are \(148\), \(1665\), and \(9136\) at field orders \(2\), \(3\), and \(4\), respectively. For two operators on a four-space over \(\mathbb F_2\), the total is \(8296\). These finite tests corroborate, but do not prove, the universal statements.

## Relationship to prior work
Morrison (1980) describes representations and irreducible components for the two-loop square-zero local algebra, using the reduction of a module to two rectangular maps. Schröer (2002/2004) classifies irreducible components for varieties of two nilpotent matrices annihilating each other. Huang (2021/2022) counts unrefined pairs of mutually annihilating matrices and their nilpotent variants using generating functions. Ram (2015/2016) counts a different class of observable/zero-kernel matrix pairs. The contribution here is the **joint radical-image and socle-codimension** arithmetic distribution for all module sizes and all numbers of loops, with its sharp feasibility region and geometric rank-stratum structure. It does not assert that those foundational reductions, broader component classifications, or univariate counts are new.

## Limitations
The theorem counts labeled representations, not isomorphism classes. It does not provide orbit decompositions, closure-incidence relations between strata, the singular locus or nilpotent structure of the entire representation scheme, or asymptotic laws. A historically equivalent bivariate enumeration could be implicit in quiver Hall-algebra literature; no independent priority or proof audit has been performed.

## References
1. K. Morrison, *The scheme of finite-dimensional representations of an algebra*, Pacific J. Math. 91 (1980), 199–218. DOI: 10.2140/pjm.1980.91.199. Open full text: https://aimath.org/~morrison/Research/SchemeFinDimReps.pdf.
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first public arXiv submission 19 November 2002), Comment. Math. Helv. 79 (2004), 396–426.
3. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (2021).
4. S. Ram, *Counting zero kernel pairs over a finite field*, arXiv:1509.08053 (2015), Linear Algebra Appl. 495 (2016), 1–10.
