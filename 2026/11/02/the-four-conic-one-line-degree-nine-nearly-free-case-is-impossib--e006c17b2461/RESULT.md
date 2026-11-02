# The four-conic, one-line degree-nine nearly-free case is impossible

## Finding

**Theorem.** Over \(\mathbb C\), no reduced arrangement of four distinct smooth plane conics and one distinct projective line has precisely zero nodes, thirteen ordinary tacnodes, and two ordinary triple points, with no other singularities. Consequently, there is **no nearly free** degree-nine conic–line arrangement comprising exactly four smooth conics and one line and admitting only nodes, ordinary tacnodes, and ordinary triple points.

The first assertion excludes the entire weak-combinatorial type \((d,k;n_2,t,n_3)=(1,4;0,13,2)\), whether or not a defining polynomial has any special Jacobian syzygies. The second assertion uses known necessary conditions for nearly free curves.

## Assumptions and scope

Work in \(\mathbb P^2_{\mathbb C}\). Each component is smooth and reduced, all five components are distinct, and the only allowed singularities of their union are ordinary nodes (two transverse branches), ordinary tacnodes (two smooth branches with intersection multiplicity two), and ordinary triple points (three pairwise transverse smooth branches). Let \(n_2\), \(t\), and \(n_3\) be the respective numbers. A tacnode involving a line and two conics simultaneously is **not** an allowed ordinary tacnode or ordinary triple point. The degree is \(m=2k+d\), where \(k=4\) and \(d=1\).

For the nearly-free corollary, we use the conventional definition through the Jacobian saturation quotient and the exponents of a nearly free reduced plane curve; the only required properties are \(d_1+d_2=m\), \(d_1=\operatorname{mdr}(f)\), and the standard Tjurina identity.

## Proof

### Necessary numerical type

Suppose first that such an arrangement were nearly free. The bound of Dimca–Pokora as used in Gałecka's Proposition 4.1 gives
\[
\tfrac23m-2\le\operatorname{mdr}(f)=d_1\le\tfrac m2.
\]
For \(m=9\), integrality gives \(d_1=4\) and \(d_2=5\). The nearly-free Tjurina formula then gives
\[
\tau=4^2-4(9-1)+(9-1)^2-1=47.
\]
Since nodes, ordinary tacnodes, and ordinary triple points have local Tjurina numbers \(1,3,4\), respectively,
\[
n_2+3t+4n_3=47.
\]
Bézout counts intersections between the four conics and the line:
\[
4\binom{4}{2}+2\cdot4=32=n_2+2t+3n_3.
\]
Thus \(t+n_3=15\). The resulting identity \(n_2+n_3=2\) follows, and hence \(t=13+n_2\). Gałecka's Proposition 4.4 gives
\[
8k+n_2+\tfrac34 n_3\ge d+\tfrac52 t.
\]
Putting \(k=4\), \(d=1\), \(n_3=2-n_2\), and \(t=13+n_2\) gives \(33.5+0.25n_2\ge33.5+2.5n_2\), so \(n_2=0\), \(n_3=2\), and \(t=13\). This is the only numerically admissible nearly-free weak-combinatorial type for four conics and one line at degree nine.

### Common-tangent obstruction

We use the following elementary geometric fact, also proved in Dimca–Pokora, Lemma 5.1: if two smooth conics meet at exactly two ordinary tacnodes, then **no line can be tangent to both** while their union with that line has only the three allowed singularity types. Indeed, their dual conics have just two common tangent-line points, corresponding to the tangent lines at the two tacnodes: the dual intersection multiplicities are at least two at each, and Bézout's degree-four intersection forces these to be all common tangents. Adding either line creates a point with three mutually tangent branches, which is not ordinary. Equivalently, this follows from the normal forms and dual-conic argument of the cited Lemma 5.1.

Now assume for contradiction that an arrangement has \((n_2,t,n_3)=(0,13,2)\). Write its components \(L,C_1,C_2,C_3,C_4\). Let \(s\) be the number of its two ordinary triple points on \(L\). Because there are no nodes, any conic meeting \(L\) transversely must do so at an ordinary triple point. Since \(L\cdot C_i=2\), each conic either is tangent to \(L\) once, or meets \(L\) transversely at both of the two triple points on \(L\). Thus \(s\) cannot be one.

If \(s=0\), the line is tangent to all four conics and contributes precisely four tacnodes. There are therefore nine conic–conic tacnodes. The six conic pairs contribute at most two tacnodes each by Bézout, so at least one pair must contribute two. That pair has two tacnodes and both conics are tangent to \(L\), contradicting the common-tangent obstruction.

If \(s=2\), exactly two conics, say \(C_1,C_2\), pass transversely through *both* triple points on \(L\); the other two, \(C_3,C_4\), are tangent to \(L\). Therefore \(L\) contributes two tacnodes and the conic pairs must contribute eleven. The pair \((C_1,C_2)\) already intersects transversely at two points and hence can contribute at most one tacnode, while each other conic pair contributes at most two. Since there are five other pairs, eleven conic–conic tacnodes force \((C_1,C_2)\) to contribute one and **each of the remaining five pairs** to contribute two. In particular \(C_3\) and \(C_4\) meet in two tacnodes and are both tangent to \(L\). This again violates the common-tangent obstruction.

Both possibilities are impossible, proving the geometric exclusion and therefore the nearly-free corollary. \(\square\)

## Verification

The accompanying standard-library Python program `verify_incidence.py` checks the published Tjurina and Bézout equations, the resulting integer possibilities under the published inequality, and the separate upper bounds on conic–conic tacnodes for the two line-triple cases. It is a consistency checker, **not** a computational proof of the geometric common-tangent lemma. The proof above uses only the stated external theorems, Bézout, and explicit incidence reasoning. Run with `python3 verify_incidence.py`; expected output: `DEGREE9_FOUR_CONICS_EXCLUSION_OK`.

## Relationship to prior work

Gałecka (2022) classifies nearly-free conic–line arrangements in several degrees and identifies degree eight and degree nine as unresolved globally. Its Proposition 4.1 and Proposition 4.4, together with its exponents/Tjurina formulas, isolate the present numerical type but do not eliminate it. Dimca–Pokora (2022) proves the common-tangent lemma (Lemma 5.1) and classifies **free** conic–line arrangements; a free-arrangement classification alone does not cover the nearly-free case. The new step is combining the degree-nine nearly-free numerical restrictions with the placement of the two triple points on the unique line, to rule out an entire potential degree-nine component class. A published degree-eight nearly-free example addresses a different degree and does not imply the theorem.

## Limitations

The result excludes only the four-conic, one-line component type among degree-nine nearly-free arrangements. It does **not** settle the types with fewer conics or the full degree-eight/nine existence problem. It assumes characteristic zero, smooth distinct components, and precisely the three named singularities. Its originality is based on accessible literature and mathematical-record comparisons, not a proof that no earlier unindexed treatment exists. No independent external mathematical audit has been performed.

## References

1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points* (first preprint 29 April 2022), arXiv:2204.13969; *Boletín de la Sociedad Matemática Mexicana* **28**, 67 (2022), DOI: 10.1007/s40590-022-00461-4. Full paper: https://link.springer.com/article/10.1007/s40590-022-00461-4.
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, *Journal of Algebraic Combinatorics* **56**, 403–424 (2022), DOI: 10.1007/s10801-022-01116-3; especially Lemma 5.1 and Theorem 5.2. Full paper: https://link.springer.com/article/10.1007/s10801-022-01116-3.
