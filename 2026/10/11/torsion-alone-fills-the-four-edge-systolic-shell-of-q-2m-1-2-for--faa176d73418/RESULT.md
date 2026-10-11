# Torsion alone fills the four-edge systolic shell of \(Q_{2m+1,2}\) for \(m\ge4\)
## Finding
For every integer \(m\ge4\), let
\[
K_m=Q_{2m+1,2}
\]
be the Datta--Upadhyay weakly regular triangulation of the Klein bottle on the cyclic vertex set
\[
\mathbb Z/(4m+2).
\]
In the cyclic labeling, its triangular faces are
\[
A_i=\{i,i+1,i+2\},\qquad
B_i=\{i,i+2,i+2m+2\},
\]
with indices modulo \(4m+2\).

Then
\[
H_1(K_m;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2,
\]
and the minimum edge length of a simple cycle carrying nonzero integral homology is exactly \(4\).

There are exactly
\[
6m+3
\]
unoriented simple four-edge cycles carrying nonzero homology. Every one represents the unique nonzero element of order two. In particular, no simple integral homology systole has infinite-order class.

Writing \(p=2m+1\), the minimum carriers are exactly the two translation families
\[
R_i=(i,i+1,i+p,i+p-1),
\]
and
\[
S_i=(i,i+1,i+p,i+p+1).
\]
There are \(4m+2\) distinct \(R_i\) and \(2m+1\) distinct \(S_i\). Hence cyclic translation has exactly two orbits on the systolic carriers, of sizes
\[
4m+2\quad\text{and}\quad2m+1.
\]

## Assumptions and scope
A simple integral homology \(1\)-systole means a simple edge cycle of least edge length among cycles whose class in \(H_1(-;\mathbb Z)\) is nonzero. Cycles are counted up to reversal and cyclic change of starting vertex.

The theorem is restricted to \(m\ge4\). The smaller parameters have extra short-step coincidences and are not included.

The source first defines the same \(Q_{2m+1,n}\) Klein-bottle family in its original two-row labeling; a later revision gives the cyclic labeling above for \(n=2\). The topological identification with the Klein bottle gives
\[
H_1(K_m;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]

## Proof
Put
\[
p=2m+1,\qquad N=2p=4m+2,\qquad h=p-1=2m.
\]
The edge graph is the circulant graph on \(\mathbb Z/N\) whose allowed signed steps are
\[
\pm1,\qquad\pm2,\qquad\pm h.
\]
Indeed, the \(A_i\)-faces have boundary-step pattern \((1,1,-2)\), while the \(B_i\)-faces have pattern \((2,h,h)\) modulo \(N\).

For \(m\ge4\), a direct integer case split on three allowed steps whose sum is a multiple of \(N=2h+2\) shows that the only simple three-edge cycles have, up to reversal, step patterns
\[
(1,1,-2)\quad\text{or}\quad(2,h,h).
\]
Thus every graph triangle is already a face. Consequently no simple cycle of length three carries nonzero homology.

Now consider a simple four-edge cycle. The same step-sum case split shows that, up to reversal, translation, and cyclic reordering, its step multiset is one of
\[
\{-2,-1,1,2\},\qquad
\{-h,-2,2,h\},\qquad
\{-h,-1,1,h\},\qquad
\{1,1,h,h\}.
\]
The non-backtracking cyclic orderings give exactly five translation families. Three are boundaries of two adjacent faces:
\[
U_i=\partial(A_i\cup A_{i+1}),
\]
\[
V_i=\partial(B_i\cup B_{i+h}),
\]
and
\[
W_i=\partial(A_i\cup B_i).
\]
These are null-homologous. The remaining two families are precisely \(R_i\) and \(S_i\) displayed above.

To identify their integral homology class, define an integral edge cocycle \(\alpha\) by assigning value \(1\) to a positively oriented step \(+1\), value \(2\) to step \(+2\), and value \(-1\) to step \(+h\), with sign reversed when edge orientation is reversed. On an \(A_i\)-face the sum is
\[
1+1-2=0,
\]
and on a \(B_i\)-face it is
\[
2-1-1=0,
\]
so \(\alpha\) is a cocycle. It is nonzero on homology because the Hamiltonian cycle using all \(+1\)-edges evaluates to \(N\). Directly,
\[
\alpha(R_i)=\alpha(S_i)=0.
\]
Since \(H_1(K_m;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\), the kernel of the induced nonzero map to \(\mathbb Z\) is exactly the torsion subgroup.

It remains to rule out the zero class. Define a mod-two edge cocycle \(\beta\) to vanish on the \(\pm1\)- and \(\pm2\)-edges and, on an \(h\)-edge, to equal the parity of either endpoint. This is well-defined because \(h\) is even. Each \(A_i\)-face evaluates to zero, and the two \(h\)-edges of every \(B_i\)-face have the same endpoint parity, so \(\beta\) also vanishes on every face boundary. But
\[
\beta(R_i)=\beta(S_i)=1.
\]
Therefore every \(R_i\) and \(S_i\) is nonzero and lies in the torsion subgroup, hence represents the unique order-two class.

There are \(N=4m+2\) distinct \(R_i\). The cycles \(S_i\) satisfy
\[
S_{i+p}=S_i
\]
as unoriented cycles, and these are the only repetitions, so there are \(p=2m+1\) of them. Thus the complete nonzero four-cycle count is
\[
N+p=6m+3.
\]
Since no three-edge cycle is homologically nonzero, the simple integral homology \(1\)-systole is exactly \(4\).

## Verification
The accompanying `verify.py` independently reconstructs the cyclic complexes and checks the algebraic cocycle identities. As a finite sanity sweep, it exhausts all graph triangles and simple four-cycles for every parameter \(4\le m\le20\), verifies that triangles are exactly faces, verifies that all four-cycles are precisely the five families \(U,V,W,R,S\), checks the three two-face boundary identities, checks \(\alpha(R)=\alpha(S)=0\) and \(\beta(R)=\beta(S)=1\), and verifies the two translation-orbit sizes.

The finite sweep is corroborative only; the all-parameter theorem is proved by the step-sum classification and cocycle argument above.

Exact replay output:

`VERIFY_OK theorem_family=Q_{2m+1,2} parameter_range=m>=4
proof_identities=A_faces+B_faces alpha_cocycle beta_cocycle R/S_detection
finite_exhaustive_sanity=m=4..20 triangles=faces quads=U|V|W|R|S
systole_length=4 minimizers=6m+3 all_unique_order2_class=yes
translation_orbits=4m+2,2m+1`

## Relationship to prior work
Datta and Upadhyay introduced the general \(Q_{2m+1,n}\) degree-regular Klein-bottle family in the first public version of their paper and explicitly state that it triangulates the Klein bottle. The first version also notes that only the smallest member \(Q_{5,2}\) had appeared in their earlier work. The revised paper supplies the especially simple cyclic presentation of \(Q_{2m+1,2}\) used here.

The inspected paper studies degree regularity, weak regularity, isomorphism classes, induced short cycles in related members, and Möbius-strip boundaries. Full-text searches of the exact source for homology and for four-cycle statements did not locate the theorem above. Focused literature searches using the family notation, Klein-bottle aliases, four-cycle terminology, homology-systole terminology, torsion terminology, and the exact \(6m+3\) count likewise did not locate a covering statement.

## Limitations
The theorem concerns simple edge length in this particular infinite triangulation family. It does not claim that length four is minimal across all triangulations of the Klein bottle, nor does it classify longer representatives of the free homology summand.

The argument uses the standard integral homology of the Klein bottle after the exact simplicial family has been identified. The explicit cocycles prove that the listed minimum carriers lie in, and nontrivially detect, its torsion subgroup.

An unindexed historical computation of these cyclic maps could contain some or all of the same four-cycle census.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:`math/0403433v1`, first submitted 2004-03-25.
2. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:`math/0403433v2`; published in *Proceedings of the Indian Academy of Sciences (Mathematical Sciences)*, DOI:`10.1007/BF02829658`.
