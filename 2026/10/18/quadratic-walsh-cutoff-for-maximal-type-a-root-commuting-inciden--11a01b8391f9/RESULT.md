# Quadratic Walsh cutoff for maximal type-A root-commuting incidence

## Finding

Let \(n\ge2\), let \(k\) be any field, and let \(E_{ij}\in\mathfrak u_n(k)\), \(1\le i<j\le n\), be the standard matrix units in the Lie algebra of strictly upper-triangular matrices. Form the graph whose vertices are these \(\binom n2\) distinguished positive-root vectors and whose edges join distinct commuting vectors. A **maximal root clique** means inclusion-maximal among subsets of these distinguished vectors, not necessarily maximal among arbitrary linear combinations.

For every \(S\subseteq\{1,\ldots,n\}\) with \(1\in S\) and \(n\notin S\), put
\[
C_S=\{E_{ij}:i<j,\ i\in S,\ j\notin S\}.
\]
All maximal root cliques are exactly the distinct \(C_S\); thus there are \(2^{n-2}\) of them. Define the integral root-incidence matrix \(B_n\) with rows indexed by these \(S\), columns by all pairs \((i,j)\) with \(i<j\), and entries \((B_n)_{S,(i,j)}=\mathbf1_{E_{ij}\in C_S}\). Put \(m=n-2\) and
\[
D_n=1+m+\binom m2.
\]
**Integral incidence theorem:** \(B_n\) has rank \(D_n\) over \(\mathbb Q\), and each of its \(D_n\) nonzero Smith invariant factors equals \(1\). In particular, its integral cokernel is free of rank \(2^m-D_n\). The intersection Gram matrix \(G_n=B_nB_n^{\mathsf T}\), whose \((S,T)\)-entry is \(|C_S\cap C_T|\), has the same rational rank and the same rational kernel as \(B_n^{\mathsf T}\).

Identify a row with a subset \(A\subseteq I=\{2,\ldots,n-1\}\), via \(S=\{1\}\cup A\), and write \(e_A\) for its standard basis vector in \(\mathbb Z^{2^m}\). For each \(J\subseteq I\), set
\[
v_J=\sum_{A\subseteq J}(-1)^{|J|-|A|}e_A.
\]
Then an explicit **integral basis** of \(\ker_{\mathbb Z}(B_n^{\mathsf T})\) is
\[
\boxed{\{v_J:J\subseteq I,\ |J|\ge3\}.}
\]
Over \(\mathbb Q\), the same kernel is the span of the Walsh characters
\[
\chi_J(A)=\prod_{i\in J}(2\mathbf1_{i\in A}-1),\qquad |J|\ge3.
\]
Its dimension is \(\sum_{r=3}^{m}\binom mr=2^m-D_n\), interpreted as zero when \(m<3\). Thus the **first exact failure of recovery from all single-root incidences occurs at \(n=5\)**: eight maximal cliques have seven linearly independent root-incidence profiles and one integral relation. For every \(n\), all low-degree (degree at most two) source/sink statistics are recoverable, while every higher-degree Walsh mode is invisible to every individual positive root.

As a separate exact size enumerator, let \(\left[{a\atop b}\right]_q\) be the Gaussian polynomial (counting binary words with \(b\) source symbols, \(a-b\) sink symbols, weighted by their number of sink-before-source pairs). Then the maximal-clique size polynomial is
\[
\boxed{M_n(z)=\sum_{s=1}^{n-1}z^{s(n-s)}\left[{n-2\atop s-1}\right]_{z^{-1}}.}
\]
In particular, every maximal clique has size between \(n-1\) and \(\lfloor n^2/4\rfloor\), and exactly \(n-1\) of them have minimum size \(n-1\).

## Assumptions and scope

All matrix-unit commutation statements hold over arbitrary fields, including characteristic two, because the relevant matrix-unit products have disjoint nonzero positions when one is nonzero. The incidence matrix is integer-valued and independent of \(k\). Smith invariants and integral kernels are over \(\mathbb Z\); the Walsh and Gram statements concern characteristic zero. Only **basis root vectors** are graph vertices. The theorem does not classify all maximal abelian Lie subalgebras or all commuting arbitrary matrices in \(\mathfrak u_n(k)\).

## Proof

**1. Reduction to source/sink cuts.** The multiplication rule is \(E_{ij}E_{ab}=\delta_{ja}E_{ib}\); for \(i<j\) and \(a<b\), the reverse product cannot be nonzero simultaneously with the forward product. Hence two distinct root units commute exactly when \(j\ne a\) and \(b\ne i\). Regard \(E_{ij}\) as an oriented arc \(i\to j\) on the naturally ordered labels. A set of arcs is pairwise commuting precisely when no vertex serves both as an arc source and an arc target. Therefore every commuting set lies inside \(C_S\) for some cut \(S\) of sources versus sinks, assigning unused labels arbitrarily, with \(1\in S\), \(n\notin S\). The latter endpoint choices are always possible because all arcs point forward.

Every \(C_S\) is maximal: if \(E_{ab}\notin C_S\), either \(a\notin S\), in which case \(E_{1a}\in C_S\) does not commute with it, or \(b\in S\), in which case \(E_{bn}\in C_S\) does not commute with it. These witnesses exist since \(a<b\), \(1\in S\), and \(n\notin S\). Conversely a maximal commuting set must equal the containing \(C_S\). Each source \(i\in S\) emits \(E_{in}\), and each sink \(j\notin S\) receives \(E_{1j}\); therefore the cut is uniquely determined by its clique. This proves the classification and the count.

**2. Boolean polynomial model and rank.** Write \(x_i=\mathbf1_{i\in A}\), \(i\in I\). Each column \(f_{ij}(A)=(B_n)_{A,(i,j)}\) is one of
\[
f_{1n}=1,\quad f_{in}=x_i,\quad f_{1j}=1-x_j,\quad f_{ij}=x_i(1-x_j)\quad(2\le i<j\le n-1).
\]
The columns therefore lie in the span of the \(D_n\) distinct squarefree monomials \(1,x_i,x_ix_j\). Conversely \(1=f_{1n}\), \(x_i=f_{in}\), and \(x_ix_j=f_{in}-f_{ij}\), so these monomials are in the **integral column span**. Squarefree monomials are linearly independent as functions on the Boolean cube: evaluating them at the \(D_n\) indicator vectors of subsets of size at most two gives an inclusion matrix triangular with diagonal entries one when subsets are ordered by size. Consequently \(B_n\) has rational rank \(D_n\). The same integer column operations, together with that unit-determinant evaluation minor, produce a \(D_n\times D_n\) minor of \(B_n\) of determinant \(\pm1\). It follows that all nonzero Smith factors equal one and that the integer cokernel has no torsion.

**3. Complete integral and rational kernels.** For any squarefree monomial \(x_H=\prod_{i\in H}x_i\) of degree at most two, direct inclusion-exclusion gives
\[
\sum_{A\subseteq J}(-1)^{|J|-|A|}x_H(\mathbf1_A)
=\begin{cases}1,&H=J,\\0,&H\ne J\end{cases}
\]
when \(|J|\le2\), and gives zero for every \(|J|\ge3\). (The equality follows by summing over the coordinates in \(J\setminus H\); if \(H\not\subseteq J\) every term vanishes.) Thus \(B_n^{\mathsf T}v_J=0\) for \(|J|\ge3\), while the images for \(|J|\le2\) are independent because they extract distinct coefficients of the polynomial column basis. The vectors \(v_J\) for **all** subsets \(J\subseteq I\) form an integer basis of \(\mathbb Z^{2^m}\): their matrix in the \(e_A\) basis is triangular with unit diagonal. Therefore those with \(|J|\ge3\) form the asserted complete integral kernel basis.

The rational Walsh characters \(\chi_J\) form an orthogonal basis of functions on the Boolean cube. A Walsh character of degree at least three is orthogonal to every polynomial of degree at most two, hence lies in \(\ker B_n^{\mathsf T}\). Their number is \(2^m-D_n\), equal to the rank-computed nullity, proving equality. Finally, for a rational row vector \(w\), \(w^{\mathsf T}G_nw=\|B_n^{\mathsf T}w\|_2^2\), so \(\ker_{\mathbb Q}G_n=\ker_{\mathbb Q}B_n^{\mathsf T}\).

**4. Clique sizes.** For a cut with \(s=|S|\), there are \(s(n-s)\) ordered source/sink pairs if order restrictions are ignored. Each sink occurring before a source removes exactly one candidate root. The first position is always a source and the last always a sink; the remaining \(n-2\) positions form a binary word with \(s-1\) sources. The Gaussian polynomial weights these words by precisely the number of removed pairs, which proves \(M_n(z)\). Every cut includes the distinct roots from the first source to all sinks and from all sources to the last sink, giving at least \(|S|+(n-|S|)-1=n-1\) roots. Equality holds exactly when no interior source precedes an interior sink, i.e. the interior symbols consist of sinks followed by sources; there are \(n-1\) such choices. The upper bound \(s(n-s)\le\lfloor n^2/4\rfloor\) is attained for an initial segment \(S\) of size nearest \(n/2\).

## Verification

Run `python3 verify.py` in the same directory. This standalone standard-library checker evaluates matrix-unit products literally and exhaustively enumerates every clique and its inclusion-maximality for \(2\le n\le6\). For \(2\le n\le9\), it independently constructs the full incidence matrices, checks their expected rank modulo two different large primes, verifies every high-degree Walsh character and every proposed integral finite-difference vector against all root columns, and compares the clique-size histograms with the Gaussian-polynomial recurrence. The observed terminal line is `VERIFY_OK_ROOT_WALSH n=2..9; exact maximal cliques n=2..6; modular rank, Walsh and integral-difference kernels n=2..9`. These finite tests corroborate but do not establish the arbitrary-\(n\) assertions; the proof above does.

## Relationship to prior work

Classical work on abelian positive-root sets and upper-triangular nilpotent Lie algebras motivates the objects. Panyushev [1] studies the root poset and its **abelian ideals**, a stronger order-ideal condition than arbitrary maximal commuting subsets of distinguished root vectors. Benjumea, Núñez and Tenorio [2] determine maximal *dimension* of arbitrary abelian subalgebras, not the complete labeled root-set incidence kernel. Lawther [3, Chapter 2, §2.1] explicitly describes source/sink cuts as maximal abelian subsets of the **full signed type-A root system** up to Weyl conjugacy; the elementary source/sink structure itself is not claimed as a new classification of full-root-system objects. The present theorem instead isolates positive-root cliques with fixed total order and computes their **integral incidence relations**, rational Walsh invisibility and exact size distribution. These incidence statements are not stated in the inspected corresponding primary sections. Ceballos, Núñez and Tenorio [4] give a maximal-dimension algorithm, not this incidence reconstruction statement.

## Limitations

The kernel theorem is a result about incidence of individually distinguished positive-root vectors, not about all abelian subalgebras; no assertion is made that these families exhaust the latter. The rank of the positive semidefinite Gram matrix is asserted over characteristic zero, not for its reduction modulo arbitrary primes. The complete formulas are proved for every \(n\ge2\), but numerical checking is bounded. Priority beyond the inspected primary sections, especially alternative terminology for incidence matrices of root-commuting sets, is not exhaustively established. No independent mathematical audit has been performed.

## References

[1] D. I. Panyushev, *The poset of positive roots and its relatives*, arXiv:math/0502385 (first posted 17 February 2005), https://arxiv.org/abs/math/0502385.

[2] J. C. Benjumea, J. Núñez, and Á. F. Tenorio, *The maximal Abelian dimension of linear algebras formed by strictly upper triangular matrices*, Theoretical and Mathematical Physics 152 (2007), 1225–1233, doi:10.1007/s11232-007-0107-z.

[3] R. Lawther, *Maximal Abelian Sets of Roots*, Memoirs of the American Mathematical Society 250, no. 1192 (2017), accepted manuscript https://api.repository.cam.ac.uk/server/api/core/bitstreams/0a21d500-af57-4175-96db-50c80aaeae7c/content, especially Chapter 2, §2.1.

[4] M. Ceballos, J. Núñez, and Á. F. Tenorio, *Computing abelian subalgebras for linear algebras of upper-triangular matrices from an algorithmic perspective*, Analele Științifice ale Universității Ovidius Constanța 24 (2016), 137–147, doi:10.1515/auom-2016-0032.
