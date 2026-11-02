# Abelian-subalgebra spectra of graphical Lie algebras and the subgraph-component polynomial

## Finding

For every finite simple graph \(G\), the complete finite-field census of abelian subalgebras of its graphical two-step nilpotent Lie algebra is an explicit transform of the already known vertex-induced subgraph-component polynomial \(Q_G(X,Y)\). The abelian subspace Grassmannians admit support strata with explicit nonemptiness and smooth irreducible dimensions. Conversely, the complete horizontal abelian-subspace spectrum over all finite fields determines \(Q_G\) exactly. In particular, the known nonisomorphic ten-vertex trees with identical \(Q_G\) give nonisomorphic graphical Lie algebras over odd-characteristic fields with identical abelian-subalgebra counts in every dimension and over every finite extension.

Let \(n=|V(G)|\), \(z=|E(G)|\), and let \(q\) be any prime power. Define
\[
Q_G(X,Y)=\sum_{S\subseteq V(G)}X^{|S|}Y^{c_G(S)},\qquad c_G(\varnothing)=0,
\]
where \(c_G(S)\) is the number of connected components of the induced graph \(G[S]\). Let \(\mathcal L_G\) have basis \(v_i\) for vertices and central basis \(z_{ij}\) for edges, with \([v_i,v_j]=z_{ij}\) for edges in the chosen order and zero otherwise. Write \(U=\mathcal L_G/[\mathcal L_G,\mathcal L_G]\cong\mathbb F_q^n\). Let \(B_r(G;q)\) count \(r\)-dimensional subspaces \(W\le U\) for which the commutator vanishes on \(W\times W\). Put
\[
[j]_q=\frac{q^j-1}{q-1},\quad
\Gamma_r(q)=\prod_{i=0}^{r-1}(q^r-q^i),\quad
\genfrac{[}{]}{0pt}{}{r}{j}_q=\prod_{i=0}^{j-1}\frac{q^{r-i}-1}{q^{j-i}-1}.
\]
Empty products equal one. For every \(0\le r\le n\),
\[
\boxed{B_r(G;q)=\frac{1}{\Gamma_r(q)}
\sum_{j=0}^{r}(-1)^{r-j}q^{\binom{r-j}{2}}
\genfrac{[}{]}{0pt}{}{r}{j}_q\,Q_G(q-1,[j]_q).}
\tag{1}
\]
This formula includes \(B_0=1\). For every \(0\le d\le n+z\), the number \(A_d(G;q)\) of all \(d\)-dimensional abelian Lie subalgebras of \(\mathcal L_G(\mathbb F_q)\) is
\[
\boxed{A_d(G;q)=\sum_{r=\max(0,d-z)}^{\min(n,d)}
B_r(G;q)\genfrac{[}{]}{0pt}{}{z}{d-r}_q
q^{r(z-d+r)}.}
\tag{2}
\]

For every \(r\ge1\), the locus of abelian \(r\)-planes in \(U\) has a locally closed stratum with exact nonzero coordinate support \(S\subseteq V(G)\). This stratum is nonempty exactly when \(c_G(S)\ge r\); whenever nonempty, it is smooth and geometrically irreducible, with dimension
\[
\boxed{|S|+(r-1)c_G(S)-r^2.}\tag{3}
\]
The empty support gives the unique \(r=0\) point.

For every fixed \(q\), the complete list \(B_0(G;q),\ldots,B_n(G;q)\) determines the univariate polynomial \(Q_G(q-1,Y)\). Consequently two graphs have equal horizontal abelian-subspace profiles in every dimension over every finite field if and only if their subgraph-component polynomials agree. No claim is made that this profile is a complete isomorphism invariant of the Lie algebra.

For the five-vertex path \(P_5\), an example involving nonmaximal abelian planes, \(B_2(P_5;q)=4q^2+q+1\) and \(B_3(P_5;q)=1\). Its full Lie algebra has four central edge basis elements, so \(A_2(P_5;2)=8619\).

## Assumptions and scope

The graph is finite, simple, undirected, and has at least one vertex; isolated vertices are allowed. The field may have any characteristic, including two: the bracket is bilinear and alternating with independent edge coordinates, and the Jacobi identity holds because all brackets are central. The formula \(Q_G\) uses *vertex-induced* connected components, not the number of edge-containing connected components or the usual edge-random-cluster polynomial. The subspaces \(W\le U\) are totally isotropic for the \(\bigwedge^2 U\to[\mathcal L_G,\mathcal L_G]\) commutator map, rather than subspaces of a chosen complement dependent on an arbitrary splitting. In formulas (1) and (2), the Gaussian coefficient is zero outside its usual integer range.

## Proof

**1. Bracket minors and support.** Choose a basis of an \(r\)-plane \(W\le U\) and put it as the rows of a full-row-rank \(r\times n\) matrix \(M\). For each edge \(\{i,j\}\), the corresponding central coordinate of the bracket of two rows is the \(2\times2\) minor of the columns \(M_i,M_j\). Thus \([W,W]=0\) precisely when adjacent columns are dependent. On the exact nonzero support \(S=\{i:M_i\ne0\}\), this forces all columns in a connected component of \(G[S]\) to lie on one projective line. Conversely, any assignment of a line to each component and a nonzero vector on that line to each supported vertex satisfies all edge minors. The row rank is \(r\) precisely when the component lines span \(\mathbb F_q^r\).

**2. The spanning-projective-line count.** Write \(c=c_G(S)\) and let \(F_r(c;q)\) count ordered \(c\)-tuples of projective lines in \(\mathbb F_q^r\) whose linear span is full. The number of lines in a fixed \(j\)-subspace is \([j]_q\). Subspace-lattice Möbius inversion therefore gives
\[
F_r(c;q)=\sum_{j=0}^{r}(-1)^{r-j}q^{\binom{r-j}{2}}
\genfrac{[}{]}{0pt}{}{r}{j}_q[j]_q^c.
\tag{4}
\]
Here the Möbius function of an interval of codimension \(h\) in the subspace lattice is \((-1)^h q^{\binom h2}\). Once the component lines are fixed, each supported column has exactly \(q-1\) choices, so the number of full-rank \(r\times n\) matrices with exact support \(S\) is \((q-1)^{|S|}F_r(c;q)\). Every \(r\)-plane has exactly \(\Gamma_r(q)=|\operatorname{GL}_r(\mathbb F_q)|\) ordered row bases, hence
\[
B_r(G;q)=\Gamma_r(q)^{-1}\sum_{S\subseteq V(G)}(q-1)^{|S|}F_r(c_G(S);q).
\tag{5}
\]
Interchanging the two finite sums in (5) and applying the definition of \(Q_G\) proves (1). For \(r=0\), only the empty support contributes; (1) agrees with the unique zero subspace.

**3. Geometric support strata.** Work over an algebraic closure. For each of the \(c\) components of \(G[S]\), choose one nonzero representative vector \(w_C\in\mathbb A^r\setminus\{0\}\) and choose a nonzero scalar for every other column in that component. This gives the open full-span part of \((\mathbb A^r\setminus\{0\})^c\times(\mathbb G_m)^{|S|-c}\). It is smooth and irreducible of dimension \(cr+|S|-c\) and is nonempty if and only if \(c\ge r\). Changing the ordered basis of \(W\) is the free \(\operatorname{GL}_r\) action on full-row-rank matrices. Its quotient is exactly the support stratum in the Grassmannian. The quotient is a smooth geometrically irreducible principal-bundle quotient, so subtracting \(r^2\) yields (3). No assertion about irreducibility of the *closure* of distinct strata being a separate component is needed.

**4. Count actual Lie subalgebras.** Let \(Z=[\mathcal L_G,\mathcal L_G]\cong\mathbb F_q^z\). If \(H\le\mathcal L_G\) is an abelian subalgebra, its image \(W\le U\) has rank \(r\) and is bracket-isotropic, and \(K=H\cap Z\le Z\) has dimension \(t=d-r\). Conversely choose such \(W,K\). The possible lifts of \(W\) into \((\mathcal L_G/K)\) are graphs of linear maps \(W\to Z/K\), of which there are \(q^{r(z-t)}\). Because brackets only depend on projected elements, every lift is abelian, and the triple \((W,K,\text{lift})\) determines \(H\) uniquely. Summing over \(r+t=d\) proves (2). Isolated vertex directions are contained in \(U\) and cause no exception.

**5. Recovery of the graph polynomial.** At any fixed \(q\), \(B_1(G;q)=[n]_q\) reveals \(n\). Multiply (1) by \(\Gamma_r(q)\). It is a triangular linear system in the unknowns \(Y_j=Q_G(q-1,[j]_q)\) for \(0\le j\le n\), because the coefficient at \(j=r\) is one. Therefore the horizontal counts recover all \(Y_j\). The integers \([0]_q,\ldots,[n]_q\) are distinct, and \(\deg_Y Q_G\le n\), so interpolation determines \(Q_G(q-1,Y)\). Varying \(q\) through arbitrarily large prime powers gives infinitely many distinct \(q-1\), uniquely recovering the polynomial in \(X,Y\). The reverse implication is immediate from (1).

**6. A nonclassification boundary and a path example.** Tittmann–Averbouch–Makowsky, Proposition 3, exhibit two nonisomorphic ten-vertex trees with the same \(Q_G\). Both have nine edges, so (1) and (2) give the same complete abelian-subspace and abelian-subalgebra counts over every finite field. Mainkar's graph-isomorphism theorem implies the associated Lie algebras are nonisomorphic in odd characteristic; this statement is not extended to characteristic two without a separate isomorphism argument. For paths, distinguishing an absent/present terminal vertex gives
\[
Q_{P_0}=1,\quad Q_{P_1}=1+XY,\quad
Q_{P_n}=(1+X)Q_{P_{n-1}}-X(1-Y)Q_{P_{n-2}}\quad(n\ge2).
\]
Substitution in (1) gives the stated \(P_5\) values. Formula (2) gives the stated \(8619\) abelian two-planes for \(q=2\).

## Verification

The included standalone `checks/check_abelian_graph_lie.py` enumerates reduced-row-echelon subspaces independently of the graph-component formula. It verifies every graph of order at most four over \(\mathbb F_2\), with direct enumeration of *all* abelian subalgebras for graphs of order at most three. Selected additional cases over \(\mathbb F_3,\mathbb F_4,\mathbb F_5\) test nonprime extension-field arithmetic, higher-rank planes, and graphs with isolated vertices. The script separately performs the triangular inverse transform and the path polynomial recurrence. It reports `GRAPH_LIE_ABELIAN_SUBALGEBRA_CENSUS_OK 84`. The proof is mathematical and does not extrapolate computational exhaustiveness to untested dimensions.

## Relationship to prior work

The graphical Lie-algebra construction and graph-isomorphism theorem are from Mainkar (2013, building on Dani–Mainkar). The subgraph-component polynomial \(Q_G\), its graph-theoretic meaning, and the existence of indistinguishable nonisomorphic ten-vertex trees are from Tittmann, Averbouch and Makowsky (2008/2011). None is represented as a new definition or discovery. Prior work on maximal abelian ideals of these algebras already describes and counts the maximum-dimensional stratum; the claim here is the *all-dimensional* finite-field subalgebra census, smooth support-stratum structure, and equivalence of the complete horizontal spectrum with \(Q_G\). Rossmann (2022) counts conjugacy classes of graphical groups, not subalgebra dimensions. Aldi et al. (2025/2026) develop independence polynomials and dimension bounds for abelian subalgebras, not the all-rank finite-field point counts. Standard projective-space and subspace-lattice enumeration are used explicitly, not claimed as new.

## Limitations

The results apply to graphical two-step nilpotent Lie algebras attached to finite simple undirected graphs; they are not formulas for arbitrary two-step nilpotent Lie algebras. The support-stratum statement concerns reduced varieties and does not classify their closure components or nonreduced defining schemes. The graph-isomorphism boundary is asserted only for odd characteristic, as supported by the cited theorem. The counting formulas require finite fields; the geometric statement holds over arbitrary algebraically closed fields. These results have not undergone independent mathematical audit. Although the accessible closely relevant sources were checked, an unlocated equivalent earlier interpretation or general theorem remains a priority risk.

## References

1. P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147, first public 2008-12-22, European Journal of Combinatorics 32 (2011), 954–974, DOI:10.1016/j.ejc.2011.03.017. Definition of \(Q_G\), Proposition 3 and the nonisomorphic tree pair.
2. M. G. Mainkar, *Graphs and Two-Step Nilpotent Lie Algebras*, arXiv:1310.3414v1, 2013-10-12, Groups, Geometry, and Dynamics 9 (2015), 55–65, DOI:10.4171/GGD/305. Graphical construction and Theorem 1.1.
3. T. Rossmann, *Enumerating Conjugacy Classes of Graphical Groups over Finite Fields*, Bulletin of the London Mathematical Society 54 (2022), 1923–1943, DOI:10.1112/blms.12665.
4. M. Aldi, T. Gabrielsen, D. Grandini, J. Harris, K. Kelley, *Independence Polynomials of 2-Step Nilpotent Lie Algebras*, arXiv:2504.19836v1, 2025-04-28, Journal of Pure and Applied Algebra 230 (2026), 108169.
