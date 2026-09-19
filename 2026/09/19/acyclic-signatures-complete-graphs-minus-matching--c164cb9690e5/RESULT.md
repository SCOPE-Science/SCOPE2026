# Factorial acyclic signatures for complete graphs minus a matching

## Statement

Let
\[
G_{r,s}=K_{\underbrace{2,\ldots,2}_{r},\underbrace{1,\ldots,1}_{s}}
       =K_{2r+s}-M_r,
\]
where \(M_r\) is a matching of size \(r\).  Order the multipartite parts, and
let \(D_{r,s}\) be the acyclic orientation in which every edge is directed
from the earlier part to the later part.  Following Mühlherr--Poullot, define
\[
\Psi(D;t)=\sum_{A\in\mathcal{AO}(G)}t^{\operatorname{rk}_D(A)},
\qquad
\sigma(D)=\Psi(D;-1),
\]
where \(\operatorname{rk}_D(A)\) is the number of edges on which \(A\) and
\(D\) disagree.

Then
\[
\boxed{
\sigma(D_{r,s})=
\begin{cases}
(-1)^{\lfloor r/2\rfloor}r!,&s=0,\\[2mm]
(-1)^{r/2}r!,&s=1\text{ and }r\text{ is even},\\[2mm]
0,&s\ge2\text{ or }(s=1\text{ and }r\text{ is odd}).
\end{cases}}
\]

Changing the reference acyclic orientation can only change the sign of
\(\sigma\), so its magnitude and its vanishing are graph invariants.  In
particular,
\[
|\sigma(K_{2r}-M_r)|=r!
\]
for every \(r\), while
\[
|\sigma(K_{2r+1}-M_r)|=
\begin{cases}
r!,&r\text{ even},\\
0,&r\text{ odd}.
\end{cases}
\]

Consequently, the acyclic-orientation graph \(\mathcal{AO}(K_{2r}-M_r)\) is
not Hamiltonian for every \(r\ge2\), and
\(\mathcal{AO}(K_{2r+1}-M_r)\) is not Hamiltonian for every even \(r\ge2\).
The zero-signature cases are not asserted to be Hamiltonian; the parity
obstruction is simply inconclusive there.

## Proof

We use a finite signed orientation algebra.  The slightly more general setup
for complete multipartite graphs makes the cancellation transparent.

Let \(G=K_{P_1,\ldots,P_p}\) have vertex parts \(P_1,\ldots,P_p\).  Introduce
one generator \(x_v\) for each vertex, subject to
\[
x_v^2=0,
\]
with generators in the same part commuting and generators in different parts
anticommuting.  For an acyclic orientation \(A\) of an induced subgraph,
choose a topological ordering and multiply its vertex generators in that
order.  This gives a well-defined monomial \(x_A\): any two linear extensions
are connected by swaps of adjacent incomparable elements, and in a complete
multipartite graph such incomparable vertices lie in the same part and hence
commute.

With the parts ordered as above, reducing \(x_A\) to part order introduces
one minus sign for every reversed cross-part edge.  Thus, on the full vertex
set, the coefficient of the canonical full monomial is exactly
\(\sigma(D)\).

Define
\[
\mathcal F
 =\sum_{U\subseteq V(G)}\ \sum_{A\in\mathcal{AO}(G[U])}x_A
\]
and
\[
\mathcal C
 =\sum_{I\text{ independent}}(-1)^{|I|}x_I.
\]
We claim
\[
\mathcal F\mathcal C=1.
\]
Indeed, fix any nonempty acyclic orientation \(H\).  The factorizations that
contribute its monomial to \(\mathcal F\mathcal C\) are obtained by choosing
an arbitrary subset \(I\) of the sinks of \(H\) as the final independent
layer.  The sink set is nonempty and independent, so the total coefficient is
\[
\sum_{I\subseteq\operatorname{Sink}(H)}(-1)^{|I|}=0.
\]
Only the empty orientation survives.  Hence \(\mathcal F=\mathcal C^{-1}\).

Put
\[
z_i=\sum_{v\in P_i}x_v.
\]
Because an independent set is contained in one part,
\[
\mathcal C
 =1+\sum_i\left(\prod_{v\in P_i}(1-x_v)-1\right)
 =\sum_i e^{-z_i}-(p-1).
\]
Write
\[
u_i=\cosh z_i-1,\qquad w_i=\sinh z_i,
\]
\[
A=1+\sum_i u_i,\qquad B=\sum_i w_i.
\]
The \(u_i\) are even and central, while \(w_iw_j=-w_jw_i\) for \(i\ne j\).
Therefore
\[
\mathcal C=A-B,
\qquad
\mathcal F=\frac{A+B}{A^2-B^2}.
\]
Since
\[
w_i^2=\sinh^2 z_i=(1+u_i)^2-1=2u_i+u_i^2,
\]
we obtain the useful identity
\[
\boxed{
\mathcal F=
\frac{1+\sum_i u_i+\sum_i w_i}
     {1+2\sum_{i<j}u_i u_j}.}
\tag{1}
\]

Now specialize to \(G_{r,s}\).  For a two-vertex part with generators
\(a_i,b_i\),
\[
u_i=a_ib_i,\qquad w_i=a_i+b_i,
\]
while for a singleton with generator \(y_j\), \(u=0\) and \(w=y_j\).
Let
\[
Q=\sum_{1\le i<j\le r}u_i u_j,
\qquad
H=(1+2Q)^{-1}=\sum_{k\ge0}(-2Q)^k.
\]
The full monomial is
\[
X=u_1\cdots u_r\,y_1\cdots y_s.
\]
A doubleton term \(a_i+b_i\) from the numerator of (1) can never contribute
to \(X\): multiplying by \(u_i\) gives zero, while omitting \(u_i\) leaves
one vertex of that part missing.  Therefore only \(1+\sum_i u_i\) and, when
there is exactly one singleton, its \(y_1\) term matter.

For any specified set of \(2k\) indices,
\[
[u_{i_1}\cdots u_{i_{2k}}]Q^k
 =k!\,(2k-1)!!
 =\frac{(2k)!}{2^k},
\]
because the contributing terms are ordered perfect matchings of those
\(2k\) indices.  Hence
\[
[u_{i_1}\cdots u_{i_{2k}}]H=(-1)^k(2k)!.
\tag{2}
\]

If \(s\ge2\), the numerator of (1) contains at most one singleton generator,
so \([X]\mathcal F=0\).  If \(s=1\), the singleton must come from the numerator,
and (2) gives zero for odd \(r\) and \((-1)^{r/2}r!\) for even \(r\).
If \(s=0\) and \(r=2k\), the constant numerator term together with (2) gives
\((-1)^k r!\).  If \(s=0\) and \(r=2k+1\), one \(u_i\) must come from the
numerator; summing over the \(r\) choices gives
\[
r\,(-1)^k(2k)!=(-1)^k r!.
\]
This proves the formula.

Finally, \(\mathcal{AO}(G)\) is bipartite according to the parity of
\(\operatorname{rk}_D\), and \(\sigma(D)\) is the difference between the two
part sizes.  A Hamilton cycle in a bipartite graph requires equal part sizes.
Thus every nonzero signature above certifies non-Hamiltonicity.

## Verification

`artifacts/verify.py` directly enumerates vertex permutations, deduplicates
the induced acyclic orientations, evaluates the signed parity sum, and compares
it with the theorem.  It checks every pair \((n,r)\) with
\(2\le n\le9\) and \(0\le r\le\lfloor n/2\rfloor\), for 28 parameter pairs in
total.  The recorded output is in `artifacts/verification.txt`.  This finite
check supports but does not replace the proof.

## Literature context and originality

Mühlherr and Poullot introduced the acyclic polynomial and its evaluation at
\(-1\) as a parity obstruction for Hamilton cycles in acyclic-orientation
graphs.  Their current arXiv version is arXiv:2609.02249v2 (September 2026).
The accessible abstract explicitly states that if \(-1\) is not a root of the
acyclic polynomial, then the graph is not \(\mathcal{AO}\)-Hamiltonian.

Carballosa, Khera and Reyes give an encoding and enumeration of acyclic
orientations of complete multipartite graphs, including a closed formula for
the total number of labelled acyclic orientations.  Their results concern
unsigned enumeration and longest-path statistics; the accessible full HTML
article was checked for the multipartite statements and did not provide the
signed edge-disagreement evaluation above.

Savage, Squire and West introduced the acyclic-orientation graph and the
corresponding even/odd bipartition relative to a reference orientation.  Their
paper treats complete graphs, cycles, chordal graphs, and some complete
bipartite graphs among other families.  Searches within the accessible PDF
found no multipartite or cocktail-party treatment.

External searches included the exact and synonymous formulations “acyclic
signature”, “acyclic polynomial at -1”, “even and odd acyclic orientations”,
“complete graph minus a matching”, “cocktail party graph”, “complete
multipartite”, “rank-generating function”, “distance enumerator”, and
Hamiltonicity/Gray-code variants.  No equivalent or stronger formula for
\(K_n-M_r\) was found.  Originality is therefore asserted only **to the best
of our knowledge**.

## Limitations

The theorem evaluates the signature at \(t=-1\); it does not give the full
acyclic polynomial \(\Psi(D;t)\).  Vanishing signature is only absence of this
particular parity obstruction and does not establish Hamiltonicity.

The full current v2 text of arXiv:2609.02249 was not completely inspected. Its accessible abstract and indexed material were checked, and exact/synonymous searches did not reveal coverage of matching complements or cocktail-party graphs.  This is the principal residual
originality risk, together with older Gray-code or hyperplane-arrangement
literature using different terminology and very recent parallel work.

## References

1. L. Mühlherr and G. Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249v2, 2026. https://arxiv.org/abs/2609.02249
2. W. Carballosa, J. Khera and F. Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, Utilitas Mathematica 125 (2025), 21–41. https://doi.org/10.61091/um125-02
3. C. D. Savage, M. B. Squire and D. B. West, *Gray Code Results for Acyclic Orientations*, Congressus Numerantium 96 (1993), 185–204. https://dwest.web.illinois.edu/pubs/aograph.pdf
