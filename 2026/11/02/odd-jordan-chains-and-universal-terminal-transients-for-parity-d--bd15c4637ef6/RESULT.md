# Odd Jordan chains and universal terminal transients for parity dynamics on tree line graphs

## Finding

Let \(T\) be any tree on \(n\ge2\) vertices. At every synchronous step, an edge of \(T\), carrying a state in \(\mathbb F_q\) with \(q\) a power of two, replaces its state by the sum of states on the other edges sharing an endpoint. Put \(M=A(L(T))\), of order \(m=n-1\), and let \(\tau(x)\) be the first entrance time of the orbit of \(x\) into its eventual periodic part. When \(n\) is odd, \(M\) is invertible and \(\tau=0\) for every state. When \(n\) is even, the zero-primary part of \(M\) consists of exactly one nilpotent Jordan block, of an odd length \(s=s(T)\) satisfying \(1\le s\le n-1\). To compute this length, for each even \(c\) let \(a_c\) be the parity of the number of spanning forests of \(T\) with exactly \(c\) components, all of odd vertex cardinality. Then \(s=\min\{c-1:a_c=1\}\). The complete first-entry counts are \(\#\{x:\tau(x)\le j\}=q^{n-1-s+j}\) for \(0\le j\le s\), hence \(\#\{\tau=0\}=q^{n-1-s}\) and \(\#\{\tau=j\}=(q-1)q^{n-2-s+j}\) for \(1\le j\le s\). In particular, \(\Pr(\tau=s)=1-q^{-1}\) is tree-independent. For every \(n=2^k\ge4\), the path has \(s=n-1\), whereas the star has \(s=1\).

This gives an exact finite, tree-combinatorial procedure for the transient-time distribution on *every* finite tree, and a universal fraction of longest transients even as their lengths vary with tree shape.

## Assumptions and scope

Trees are finite, simple, undirected, connected and have \(n\ge2\) vertices. Each original edge is a labelled site; distinct edges interact exactly when they share one endpoint. Work over any field \(\mathbb F_q\) of characteristic two, with \(q=2^b\), \(b\ge1\). Let \(m=n-1\). The line-graph adjacency matrix \(M\in\mathbb F_q^{m\times m}\) has zero diagonal. All updates are simultaneous. The entrance time is the least nonnegative \(j\) for which \(M^j x\) belongs to an eventual periodic orbit, equivalently the first time its nilpotent-primary projection is zero. A spanning forest means \((V(T),F)\) for some \(F\subseteq E(T)\), including isolated vertices, with \(c(F)\) components.

## Proof

**1. Incidence and kernel.** Let \(B\) be the \(n\times(n-1)\) vertex-edge incidence matrix, with two ones per column. In characteristic two, \(M=B^\top B\), since the diagonal of \(B^\top B\) is zero and two distinct columns have inner product one exactly when their edges meet. Leaf elimination shows \(B\) has independent columns. Its image is the even-coordinate-sum hyperplane \(H=\{v:\sum_i v_i=0\}\) because each column has even sum and \(\dim H=n-1\). Connectedness implies \(\ker B^\top=\langle\mathbf1\rangle\). Since \(B\) is injective, \(\ker M\cong H\cap\langle\mathbf1\rangle\). Thus \(\dim\ker M=0\) for odd \(n\), and \(1\) for even \(n\), over any characteristic-two field.

**2. Entire zero-primary multiplicity.** Write \(p_T(z)=\det(zI_m+M)\), which equals the characteristic polynomial over characteristic two. Sylvester's determinant identity gives \(zp_T(z)=\det(zI_n+BB^\top)\). Since \(BB^\top\) is the Laplacian of \(T\) in characteristic two, the all-minors matrix-forest determinant expansion yields the polynomial identity over integers, reduced modulo two,
\[
 zp_T(z)=\sum_{F\subseteq E(T)}z^{c(F)}\prod_{C\in\operatorname{comp}(V(T),F)}|V(C)|.
\]
For completeness, this forest identity follows by expanding \(\det(zI+BB^\top)\) by principal minors and using Cauchy–Binet: each nonzero squared maximal incidence minor represents a rooted spanning forest, and each component contributes precisely its number of choices of root. The signed incidence matrix may be used over the integers before reducing modulo two. Dividing by \(z\) gives
\[
 p_T(z)=\sum_{F\subseteq E(T)}z^{c(F)-1}\prod_{C}|V(C)|\pmod2.
\]
A coefficient survives only for forests with every component of odd order. Such a forest has \(c(F)\equiv n\pmod2\). For odd \(n\), the full tree \(F=E(T)\) is the only forest with \(c=1\), and its contribution to the constant term is \(n\equiv1\), so \(M\) is invertible. For even \(n\), only odd powers of \(z\) occur in \(p_T\), and its lowest nonzero degree is exactly \(s=\min\{c-1:a_c=1}\}\), where \(c=2,4,\dots,n\). Existence is guaranteed by the empty forest, whose coefficient at degree \(n-1\) is one. Therefore \(s\) is odd and between one and \(n-1\). From Step 1, the zero-eigenspace is one-dimensional. Consequently the entire zero-primary generalized eigenspace is a **single** Jordan block \(J_s(0)\), while the remaining \(m-s\) dimensions form an invertible component.

**3. Exact entry shells.** In the Fitting decomposition, a state enters the periodic part by time \(j\) if and only if its nilpotent component lies in \(\ker J_s^j\). This kernel has dimension \(\min(j,s)\); the invertible factor has dimension \(m-s\). Hence the number of states with \(\tau\le j\) is \(q^{m-s+j}\) for \(0\le j\le s\). Consecutive differences give every shell. For uniform initial data \(\Pr(\tau=s)=1-q^{-1}\), independently of \(T\).

**4. Opposite extrema at the same order.** For \(T=P_n\), \(L(T)=P_{n-1}\). Over characteristic two the characteristic polynomials \(f_r\) of paths satisfy \(f_0=1, f_1=z, f_r=zf_{r-1}+f_{r-2}\), and the finite-field identity \(f_{2r-1}=z f_{r-1}^2\) follows by the continuant identity (or direct induction). Iterating for \(n=2^k\) gives \(f_{n-1}=z^{n-1}\). Since the kernel is one-dimensional, \(M\) is nilpotent of exact index \(n-1\). For \(T=K_{1,n-1}\), the line graph is \(K_{n-1}\) and \(M=I+J\) with \(J\) all-ones. As \(n-1\) is odd, \(J^2=J\) in characteristic two and \(M^2=M\); its nullity is one, so its sole zero-primary block has length one.

## Verification

The embedded `verify.py` is standalone Python 3 standard-library code, independently generating tree edge-neighbor adjacency matrices and checking the incidence prediction with direct ranks, characteristic-polynomial parity, all-odd-component spanning forests, and finite trajectories. The captured `verification-output.txt` records \(1661\) checked trees and `LINE_TREE_EDGE_XOR_VERIFY_OK`. Finite checks corroborate rather than replace the above proof.

## Relationship to prior work

Cardoso, de Freitas, Martins, Robbiano and San Martín (arXiv:1306.4649v1, initially public 2013-06-19), especially their Sections 1–3, use the known incidence identity and obtain real spectral characteristic-polynomial recurrences for line graphs of caterpillars. Sciriha (1998, 1999) and Gutman–Sciriha (2001) studied singularity and nullity of line-graph adjacency over the real numbers. The classical matrix-forest identity is likewise established mathematics. Those ingredients are fully credited; none is asserted to be new. The present claim concerns **all** finite trees over characteristic-two fields, an explicit parity-forest formula for the nilpotent *algebraic* multiplicity, and the resulting exact first-periodic-entry distribution with a shape-invariant final probability. Real symmetric spectral nullity results alone do not imply the characteristic-two nilpotent Jordan lengths or transient shells.

## Limitations

The proof does not classify lengths of the eventual nonzero periodic orbits, nor simplify the forest-parity expression for every tree class. The path and star provide opposite examples without a uniqueness claim. An inaccessible older full paper could contain an equivalent characteristic-two formulation; searches and available literature cannot establish absolute historical novelty. There has been no independent audit.

## References

1. D. M. Cardoso, M. A. A. de Freitas, E. A. Martins, M. Robbiano, B. San Martín, *On the characteristic polynomial of Laplacian Matrices of Caterpillars*, arXiv:1306.4649v1 (2013-06-19), https://arxiv.org/pdf/1306.4649.
2. I. Sciriha, *On Singular Line Graphs of Trees*, Congressus Numerantium **135** (1998), 73–91; bibliographic abstract at https://www.researchgate.net/publication/234130110_On_Singular_Line_Graphs_of_Trees.
3. I. Sciriha, *The Two Classes of Singular Line Graphs of Trees*, Rend. Semin. Mat. Messina **5** (1999), 167–180, https://www.um.edu.mt/library/oar/handle/123456789/109154.
4. I. Gutman and I. Sciriha, *On the nullity of line graphs of trees*, Discrete Mathematics **232** (2001), 35–45, https://www.um.edu.mt/library/oar/handle/123456789/28364.
5. Classical matrix–forest (all-minors matrix–tree) determinant theorem; standard rooted-forest interpretation of Laplacian characteristic-polynomial coefficients.
