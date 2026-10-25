# Star-quiver Grassmannian profiles recover matroids but miss cross-ratio moduli

## Finding

Let \(Q_m\) be the inward-oriented star with labelled leaves \(1,\ldots,m\) and sink \(0\). For a field \(k\), let \(V\) be an \(r\)-dimensional vector space and let \(v_1,\ldots,v_m\) be nonzero vectors spanning \(V\). Form the representation \(M(\mathbf v)\) with \(M_i=k\), \(M_0=V\), and arrow maps \(1\mapsto v_i\). Its represented labelled matroid has rank function \(h(S)=\dim_k\langle v_i:i\in S\rangle\).

**Matroid classification and reconstruction theorem.** For every leaf subset \(S\subseteq[m]\) and \(0\le d\le r\), the quiver Grassmannian of central dimension \(d\) and leaf dimensions \(\mathbf1_S\) has the following isomorphism as a \(k\)-scheme:

\[
\operatorname{Gr}_{(d,\mathbf1_S)}(M(\mathbf v))\cong
\begin{cases}
\operatorname{Gr}(d-h(S),r-h(S)),&d\ge h(S),\\
\varnothing,&d<h(S).
\end{cases}
\]

Thus two such representations (with the same labelled star and central dimension) have isomorphic schemes separately at **every indexed dimension vector** exactly when their labelled matroids have the same rank function. The converse uses the least \(d\) for which the indexed Grassmannian is nonempty. No compatibility of the separate isomorphisms with inclusions between different dimension vectors is asserted.

If \(k=\mathbb F_q\), then their complete finite-field point-count data are

\[
 c_{S,d}=\begin{cases}{r-h(S)\brack d-h(S)}_q,&d\ge h(S),\\0,&d<h(S),\end{cases}
\]

where the bracket is a Gaussian binomial coefficient. Define the *coarse* bivariate profile
\(F_{\mathbf v}(z,t)=\sum_{S\subseteq[m]}\sum_{d=0}^r c_{S,d}z^{|S|}t^d\), and let \(A_{s,h}=\#\{S:|S|=s,\ h(S)=h\}\). Then

\[
F_{\mathbf v}(z,t)=\sum_{s=0}^{m}\sum_{h=0}^r A_{s,h}z^s t^h G_{r-h}(t;q),
\quad G_j(t;q)=\sum_{a=0}^j{j\brack a}_q t^a.
\]

For fixed \(m,r,q\), this map from \((A_{s,h})\) to \(F_{\mathbf v}\) is invertible, since \(t^hG_{r-h}(t;q)\) has lowest term \(t^h\) with coefficient one. It follows that two configurations have the same coarse profile **if and only if** their matroids have the same Tutte polynomial, because

\[
 T_{\mathcal M}(x,y)=\sum_{s,h}A_{s,h}(x-1)^{r-h}(y-1)^{s-h}
\]

and the change to this polynomial is invertible when the rank and ground-set size are fixed.

**Nonfaithfulness on bricks.** For every field \(k\) containing at least four elements, take the four-leaf star and, for each \(\lambda\in k\setminus\{0,1\}\), set

\[
v_1=(1,0),\quad v_2=(0,1),\quad v_3=(1,1),\quad v_4=(1,\lambda)\in k^2.
\]

The resulting \(M_\lambda\) are pairwise nonisomorphic **brick** representations (their endomorphism rings equal \(k\)), although the independently indexed quiver Grassmannian schemes, all finite-field point counts when applicable, and all corresponding cohomological invariants coincide. Their labelled matroid is always \(U_{2,4}\). Thus even the complete indexed family of abstract quiver Grassmannians does not reconstruct the isomorphism class of an indecomposable representation.

## Assumptions and scope

The sink direction of every arrow is essential: this statement is for maps from a one-dimensional leaf into the common central space, not for the oppositely oriented star. All leaf vectors are required to be nonzero; they span the central space. Leaf indices are fixed and cannot be permuted in the reconstruction or nonisomorphism claims. The scheme statement works over an arbitrary field; the Gaussian point-count formula requires a finite field of order \(q\). The cross-ratio family has at least two distinct parameters when \(|k|\ge4\). The profile records an indexed scheme isomorphism class for each \((d,S)\), not a diagram of incidence correspondences between different strata.

## Proof

**1. Scheme-theoretic reduction.** Let \(S\) be the set of leaves at which the desired subrepresentation has dimension one. Each leaf contributes the unique rank-one subspace of \(k\) if its dimension is one, and the unique zero subspace otherwise. The central subspace \(W\subseteq V\) must therefore contain each \(v_i\) for \(i\in S\), equivalently the fixed subspace \(L_S=\langle v_i:i\in S\rangle\). If \(d<h(S)\), no such \(W\) exists. Otherwise, the assignment \(W\mapsto W/L_S\) is a natural identification, on test schemes, with rank-\(d-h(S)\) subbundles of \((V/L_S)\otimes_k\mathcal O\) whose quotients are locally free. This gives the asserted isomorphism with an ordinary Grassmannian as a **scheme**, not just a bijection on rational points.

**2. Matroid reconstruction.** The Grassmannian is nonempty exactly at central dimensions \(d\ge h(S)\), so its first nonempty position recovers \(h(S)\). Conversely, knowing \(h(S)\) for every labelled subset fixes every displayed Grassmannian isomorphism class. No cross-subset compatibility is used.

**3. Coarse profile and Tutte reconstruction.** Over \(\mathbb F_q\), the ordinary Grassmannian has \({r-h\brack d-h}_q\) rational points. Grouping subsets by their size and rank yields the displayed polynomial. For fixed size \(s\), the coefficient of \(t^0\) recovers \(A_{s,0}\); subtracting its contribution and reading \(t^1\) recovers \(A_{s,1}\), and so forth. This lower-triangular elimination has diagonal ones and works for every prime power. The subset-rank expression for the Tutte polynomial is an invertible polynomial translation and bidegree change after \(m,r\) are fixed; hence the claimed equivalence.

**4. Nonisomorphic bricks.** All four listed vectors represent pairwise distinct lines, so their rank matroid is \(U_{2,4}\). An isomorphism \(M_\lambda\to M_\mu\) must have a central invertible map \(g\) sending each of the first three labelled lines to itself. In a two-space, a projective linear transformation fixing three distinct projective points is the identity, so \(g\) is scalar and preservation of the fourth line forces \(\lambda=\mu\). The same argument for any endomorphism (without assuming invertibility) shows that its central component is scalar, since a linear endomorphism preserving three distinct lines is scalar; the nonzero arrows force all four leaf components to equal that scalar. Thus \(\operatorname{End}(M_\lambda)=k\). A brick is indecomposable because its endomorphism ring has no nontrivial idempotents. The matroid classification already proved shows that every corresponding indexed quiver Grassmannian is isomorphic across parameters.

## Verification

The included reproducible program `check_star_quiver.py` constructs all central RREF subspaces and counts subspaces that contain each selected collection of arrow images, independently of the theoretical Gaussian calculation. It verifies 96 parameter configurations over the prime fields of orders \(2,3,5\), central dimensions \(2,3\), and leaf counts \(2,3,4,5\), totalling 1,440 labelled support-set tests; it also tests rank reconstruction and the inverse coarse transform. For the four-leaf example over \(\mathbb F_5\), it verifies identical complete counting profiles at two distinct parameters and searches all central invertible \(2\times2\) matrices with arbitrary leaf rescalings to confirm nonisomorphism. The printed success marker is `ALL_STAR_QUIVER_CHECKS_PASSED`. These finite checks do not substitute for the functorial proof over all fields.

## Relationship to prior work

Quiver Grassmannians and their point/Euler-characteristic enumerations have been studied extensively. Jun--Sistko (arXiv:2112.06291) use coefficient quivers and \(\mathbb F_1\)-methods to compute Euler characteristics for certain classes. Cerulli Irelli--Esposito--Franzen--Reineke (arXiv:1804.07736) prove cellular and cohomological results in rigid and finite/affine-type settings; these encompass some smoothness conclusions for special cases here but do not identify the displayed matroid recovery or brick-moduli obstruction. Jarra--Lorscheid--Vital (arXiv:2404.09255) develop a different, more general theory of quiver matroids and \(\mathbb F_1\)-moduli, but their inspected statements do not provide this particular star-quiver abstract-scheme classification, coarse Tutte reconstruction, or cross-ratio family. Lorscheid--Weist (arXiv:1706.00860) characterize quiver representation type by the possible geometry of quiver Grassmannians, a different assertion from recovering an individual representation. Ordinary Grassmannian counts, matroid rank functions, and the three-point rigidity of projective linear maps are classical ingredients and are not claimed as discoveries.

## Limitations

The classification applies to the stated inward stars with nonzero one-dimensional leaf maps; it is not claimed for arbitrary quivers, for higher-dimensional leaves, or for global diagrams relating the Grassmannians. Identical **abstract individual** varieties need not mean identical Plücker embeddings or identical incidence maps between strata. The nonisomorphism family requires distinct cross-ratio parameters. The completeness of the literature search and historical priority are not proven: a specialist earlier treatment of subspace-configuration representations might already imply some or all of the statements. No independent mathematical audit has been performed.

## References

1. J. Jun and A. Sistko, *Coefficient Quivers, \(\mathbb F_1\)-Representations, and Euler Characteristics of Quiver Grassmannians*, arXiv:2112.06291 (first posted 2021-12-12).
2. G. Cerulli Irelli, F. Esposito, H. Franzen, and M. Reineke, *Cell decompositions and algebraicity of cohomology for quiver Grassmannians*, arXiv:1804.07736 (first posted 2018-04-20).
3. M. Jarra, O. Lorscheid, and E. Vital, *Quiver matroids -- Matroid morphisms, quiver Grassmannians, their Euler characteristics and \(\mathbb F_1\)-points*, arXiv:2404.09255 (first posted 2024-04-14).
4. O. Lorscheid and T. Weist, *Representation type via Euler characteristics and singularities of quiver Grassmannians*, arXiv:1706.00860 (first posted 2017-06-02).
