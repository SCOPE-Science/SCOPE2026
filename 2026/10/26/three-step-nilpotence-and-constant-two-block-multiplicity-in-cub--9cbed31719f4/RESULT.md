# Three-step nilpotence and constant two-block multiplicity in cubical edge-parity dynamics

## Finding
For every integer \(d\ge2\), let \(Q_d\) be the graph on \(\mathbb F_2^d\) whose adjacent vertices differ in exactly one coordinate, and let \(G_d=L(Q_d)\) be its simple line graph. Give each vertex of \(G_d\) a binary state, updated synchronously to the XOR of the states at all distinct graph neighbours. Write \(F_d\) for the resulting linear update over \(\mathbb F_2\), \(N=2^d\) for the number of cube vertices, and \(M=d2^{d-1}\) for the number of edge-sites. Then

\[
F_d^3=0,\qquad
\operatorname{rank}F_d=N-2,\qquad
\operatorname{rank}F_d^2=N/2-2.
\]

The complete nilpotent Jordan form comprises precisely \(N/2-2\) blocks of length three, **exactly two** blocks of length two, and \((d-3)2^{d-1}+2\) blocks of length one. Consequently the zero configuration is the only recurrent configuration. The sharp maximum first-zero time is two for \(d=2\), and three for every \(d\ge3\).

For \(t=0,1,2,3\), define \(r_0=M\), \(r_1=N-2\), \(r_2=N/2-2\), \(r_3=0\). The exact number of initial states that have reached zero by time \(t\) is \(2^{M-r_t}\). In particular, when \(d\ge3\), the exact proportion first reaching zero on the third update is

\[
1-2^{-(2^{d-1}-2)}.
\]

At the one-dimensional boundary \(d=1\), the line graph has one isolated vertex and its update is the zero map; the displayed formulas for \(d\ge2\) do not extend to its second-power rank.

## Assumptions and scope
All vector spaces and matrix ranks are over \(\mathbb F_2\). A cube edge becomes one site of the line graph, and two such sites are adjacent only when the corresponding **distinct** cube edges share an endpoint. States use the synchronous open-neighbour update with no self-site term. All graphs are finite, simple, and undirected. The index \(d\) ranges over all integers at least two; statements about the sharp three-step time require \(d\ge3\). "Reaching zero by time \(t\)" means \(F_d^t x=0\), and its first-zero time is the least such \(t\).

## Proof
Let \(B\) be the \(N\)-by-\(M\) unoriented vertex-edge incidence matrix of \(Q_d\) over \(\mathbb F_2\), with two unit entries per column. Because distinct cube edges share at most one endpoint, the diagonal entries of \(B^{\mathsf T}B\) are two (hence zero in characteristic two), and its off-diagonal entries indicate shared endpoints. Thus

\[
F_d=B^{\mathsf T}B,\quad L=BB^{\mathsf T},\quad F_d^t=B^{\mathsf T}L^{t-1}B\quad(t\ge1).
\]

Cube connectivity implies that \(\ker B^{\mathsf T}\) is the one-dimensional space spanned by the all-ones vertex vector \(\mathbf j\): a vertex function with zero sum across every edge is constant. Similarly, the image of \(B\) is the codimension-one even-sum subspace \(I\) of vertex functions. Indeed, each incidence column has even coordinate sum, while the columns of a spanning tree generate all even-sum vertex vectors.

Identify the vertex function space with the group algebra \(R=\mathbb F_2[(\mathbb Z/2\mathbb Z)^d]\), whose basis is indexed by cube vertices. Let \(g_i\) denote translation by the \(i\)-th coordinate vector and put \(y_i=1+g_i\). In characteristic two, \(y_i^2=0\), so

\[
R\cong\mathbb F_2[y_1,\ldots,y_d]/(y_1^2,\ldots,y_d^2),
\]

and the even-sum subspace \(I\) is precisely the augmentation ideal of elements with zero constant coefficient when expressed in the \(y_i\) variables. The cube Laplacian \(L=BB^{\mathsf T}\) acts on \(R\) by multiplication by

\[
s=d+\sum_{i=1}^{d}g_i=\sum_{i=1}^{d}y_i.
\]

Therefore \(s^2=0\), yielding \(L^2=0\) and \(F_d^3=0\).

The all-ones vertex vector corresponds to

\[
\mathbf j=\prod_{i=1}^{d}(1+g_i)=\prod_{i=1}^{d}y_i.
\]

For \(d\ge2\), it lies in \(I\) and is nonzero, so

\[
\operatorname{rank}F_d=\dim B^{\mathsf T}(I)
=\dim I-\dim(I\cap\ker B^{\mathsf T})=(N-1)-1=N-2.
\]

The linear variable change \(z_1=s\), \(z_i=y_i\) for \(2\le i\le d\) is invertible and preserves square-zero relations. Multiplication by \(s=z_1\) therefore maps the augmentation ideal \(I\) onto the subspace with basis

\[
\left\{z_1\prod_{i\in S}z_i:\varnothing\ne S\subseteq\{2,\ldots,d\}\right\}.
\]

Hence \(\dim sI=2^{d-1}-1\). Moreover, since terms containing repeated \(y_i\) vanish,

\[
\mathbf j=s\prod_{i=2}^{d}y_i\in sI.
\]

As \(\ker B^{\mathsf T}=\langle\mathbf j\rangle\), the equation \(F_d^2=B^{\mathsf T}LB\) gives

\[
\operatorname{rank}F_d^2
=\dim B^{\mathsf T}(sI)=(2^{d-1}-1)-1=2^{d-1}-2.
\]

A nilpotent operator with cube zero has: as many size-three Jordan blocks as the rank of its square; as many size-two blocks as its rank minus twice that rank; and the remaining blocks have size one. Inserting \(\operatorname{rank}F_d=N-2\), \(\operatorname{rank}F_d^2=N/2-2\), and ambient dimension \(M=dN/2\) gives the announced multiplicities. All configurations reach zero in at most three steps, and no nonzero periodic point exists. The stated maximum first-zero times follow from whether \(\operatorname{rank}F_d^2\) is positive. Finally, rank-nullity counts the kernel of each iterate \(F_d^t\) as \(2^{M-r_t}\), proving the exact extinction-depth census. No finite verification is needed for these infinite-parameter deductions.

## Verification
The accompanying Python program `verify_cube_edge_parity.py` constructs the line graph directly by comparing cube-edge endpoint pairs, rather than using the incidence factorisation in the proof. It checks GF(2) ranks for \(F_d^t\) at \(t=0,1,2,3\) for \(d=2,\ldots,8\), verifies the zero third power, exhaustively enumerates all 16 and 4096 initial states for \(d=2,3\), respectively, checks 512 independently sampled configurations for each \(d=4,\ldots,8\), and tests the \(d=1\) boundary. Its output is included in `verify_cube_edge_parity_output.txt`; it concludes `CUBE_EDGE_PARITY_VERIFY_OK`. These finite tests corroborate but do not replace the proof.

For \(d=2\), exact first-zero counts at times \(0,1,2,3\) are \(1,3,12,0\). For \(d=3\), they are \(1,63,960,3072\). Both agree with the formulas.

## Relationship to prior work
Fish, Key and Mwambene studied binary codes derived from the **same line graphs** of \(n\)-cubes and established the binary adjacency rank \(2^n-2\) in their 2010 coding-theory work. This already covers the first-power rank and is not claimed as new here. Muthivhi's 2013 thesis, Chapter 5, reproduces the line-graph incidence factorisation and first-power rank, with attention to code parameters and permutation decoding. The additional results established here are the *second-power rank*, the complete nilpotent Jordan filtration, the sharp extinction-depth census, and the dimension-independent multiplicity of exactly two length-two blocks. The prior first-power rank alone does not imply these consequences: it leaves the lengths of nilpotent blocks undetermined.

General work on linear cellular automata provides background but not these finite cube-edge ranks. Studies of parity dynamics on distance-two cube graphs concern different graph operators; the line graph has \(d2^{d-1}\) sites, not \(2^d\). The complete 2010 article was not accessible for a full-text comparison; historical coverage therefore remains uncertain despite examination of the closely related 2013 thesis chapter.

## Limitations
Historical novelty is not certified: the complete 2010 primary article was not accessible, and unindexed equivalents cannot be excluded. The theorem concerns binary XOR and unweighted, undirected cube line graphs, not arbitrary alphabets, nonlinear excitation rules or perturbations of the graph. The asymptotic claim is specifically the probability of reaching zero **at the third update** under the uniform distribution of binary initial states. The mathematical conclusions are proved for all permitted dimensions, while program checks cover only the finite dimensions indicated above.

## References
- W. Fish, J. D. Key and E. Mwambene, "Binary codes from the line graph of the \(n\)-cube," *Journal of Symbolic Computation* 45 (2010), 800–812. DOI: https://doi.org/10.1016/j.jsc.2010.03.012.
- T. R. Muthivhi, *Codes Related to and Derived from Hamming Graphs*, University of the Western Cape MSc thesis, February 2013, Chapter 5, Sections 5.1–5.3, https://uwcscholar.uwc.ac.za/bitstreams/74fd2e17-fcb9-4f8e-a8b1-19f804fa47f0/download.
- T. Ceccherini-Silberstein and M. Coornaert, "The Garden of Eden theorem for linear cellular automata," *Ergodic Theory and Dynamical Systems* 26 (2006), 53–68, first published online 13 January 2006. DOI: https://doi.org/10.1017/S0143385705000520.
