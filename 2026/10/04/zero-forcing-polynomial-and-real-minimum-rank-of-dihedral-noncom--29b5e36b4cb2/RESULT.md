# Zero forcing polynomial and real minimum rank of dihedral noncommuting graphs

## Finding

Let \(D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) with \(n\ge3\), and let \(\Gamma_n\) be its noncommuting graph on \(D_{2n}\setminus Z(D_{2n})\). If \(N=|V(\Gamma_n)|\), then over the real symmetric minimum-rank model \[\operatorname{mr}(\Gamma_n)=2,\qquad M(\Gamma_n)=Z(\Gamma_n)=N-2.\] More precisely, the zero forcing polynomial has exactly three nonzero terms. For odd \(n\), \(N=2n-1\) and \[\mathcal Z(\Gamma_n;x)=n(n-1)x^{N-2}+Nx^{N-1}+x^N.\] For even \(n\), \(N=2n-2\) and \[\mathcal Z(\Gamma_n;x)=\frac{3n(n-2)}2x^{N-2}+Nx^{N-1}+x^N.\] Equivalently, a minimum zero forcing set is the complement of exactly two vertices: for odd \(n\), one noncentral rotation and one reflection; for even \(n\), either one noncentral rotation and one reflection, or two noncommuting reflections.

The result classifies every minimum zero forcing set, not only its size.

## Assumptions and scope

Let
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\qquad n\ge3.
\]
The noncommuting graph \(\Gamma_n\) has vertex set
\[
D_{2n}\setminus Z(D_{2n}),
\]
with distinct vertices adjacent exactly when they do not commute.

For a finite simple graph \(G\), the zero forcing polynomial is
\[
\mathcal Z(G;x)=\sum_{k=0}^{|V(G)|} z(G;k)x^k,
\]
where \(z(G;k)\) is the number of zero forcing sets of size \(k\).

The real symmetric minimum rank is
\[
\operatorname{mr}(G)=\min_{A\in\mathcal S(G)}\operatorname{rank}A,
\]
where \(\mathcal S(G)\) consists of real symmetric matrices whose off-diagonal nonzero pattern is exactly \(G\). The corresponding maximum nullity is
\[
M(G)=|V(G)|-\operatorname{mr}(G),
\]
and the standard inequality is
\[
M(G)\le Z(G).
\]

## Proof

Write the noncentral rotations as \(A\) and the reflections as \(B\).

If \(n\) is odd, the center is trivial. Hence
\[
|A|=n-1,\qquad |B|=n.
\]
Distinct rotations commute, every nonidentity rotation fails to commute with every reflection, and distinct reflections fail to commute. Therefore
\[
\Gamma_n\cong \overline{K}_{n-1}\vee K_n.
\tag{1}
\]

If \(n\) is even, the center is
\[
Z(D_{2n})=\{1,r^{n/2}\}.
\]
Hence
\[
|A|=n-2,\qquad |B|=n.
\]
Again every noncentral rotation is adjacent to every reflection. Two distinct reflections \(r^is\) and \(r^js\) commute exactly when
\[
j\equiv i+\frac n2\pmod n.
\]
Thus the reflection subgraph is the cocktail-party graph obtained from \(K_n\) by deleting a perfect matching:
\[
\Gamma_n\cong \overline{K}_{n-2}\vee\left(K_n-\frac n2K_2\right).
\tag{2}
\]

We first prove
\[
\operatorname{mr}(\Gamma_n)\le2.
\]

Use the nonsingular symmetric bilinear form
\[
H=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
For odd \(n\), assign the vector \((1,0)\) to every rotation vertex and \((1,1)\) to every reflection vertex. Pairing through \(H\) gives zero between two rotations and a nonzero value for every rotation-reflection pair and every distinct reflection pair. Therefore the resulting Gram-type matrix has exactly the graph pattern in (1) and rank \(2\).

For even \(n\), assign \((1,0)\) to every rotation vertex. Pair the reflections as
\[
r^is,\quad r^{i+n/2}s,
\qquad 0\le i<n/2.
\]
Choose distinct positive numbers
\[
t_i=2^i
\]
and assign
\[
(1,t_i),\qquad (1,-t_i)
\]
to the two vertices in the \(i\)-th commuting pair. Their \(H\)-pairing is zero. Any two reflections from different pairs have pairing
\[
\pm t_i\pm t_j\ne0,
\]
and every rotation-reflection pairing is nonzero. Hence the resulting symmetric matrix has exactly the pattern in (2) and rank \(2\).

Thus
\[
M(\Gamma_n)\ge N-2.
\tag{3}
\]

We now classify the complements of minimum zero forcing sets.

Assume first that \(n\) is odd. Consider a coloring with exactly two white vertices.

If one white vertex lies in \(A\) and the other in \(B\), then there is a blue rotation vertex. It has the white reflection as its unique white neighbor, so it forces that reflection. A blue reflection then forces the remaining white rotation. Hence every mixed white pair gives a zero forcing set.

If both white vertices lie in \(A\), then every blue reflection sees both of them and no blue rotation sees either one. No force is possible.

If both white vertices lie in \(B\), then every blue vertex sees either both white vertices or neither. Again no force is possible.

Therefore the zero forcing sets of size \(N-2\) are exactly the complements of mixed pairs, and their number is
\[
|A||B|=n(n-1).
\tag{4}
\]

Now let \(n\) be even. If the two white vertices are mixed, the same argument works: a blue rotation forces the white reflection, then a blue reflection forces the white rotation.

If both white vertices lie in \(A\), no force is possible.

Suppose both white vertices lie in \(B\). If they are a commuting reflection pair, then every blue rotation is adjacent to both and every blue reflection is also adjacent to both, so no force is possible. If they are noncommuting reflections \(x,y\), let \(x'\) be the unique reflection commuting with \(x\). Then \(x'\) is blue, is nonadjacent to \(x\), and is adjacent to \(y\); hence
\[
x'\longrightarrow y.
\]
Afterward a blue rotation forces \(x\). Thus a two-reflection white pair is forcing exactly when the pair is an edge of the cocktail-party subgraph.

The number of mixed white pairs is
\[
n(n-2),
\]
and the number of noncommuting reflection pairs is
\[
\binom n2-\frac n2=\frac{n(n-2)}2.
\]
Hence
\[
z(\Gamma_n;N-2)
=
\frac{3n(n-2)}2.
\tag{5}
\]

Equations (4) and (5) exhibit zero forcing sets of size \(N-2\). Combining this with (3) and
\[
M(\Gamma_n)\le Z(\Gamma_n)
\]
gives
\[
M(\Gamma_n)=Z(\Gamma_n)=N-2
\]
and therefore
\[
\operatorname{mr}(\Gamma_n)=2.
\]

Finally, every set of size \(N-1\) is zero forcing because \(\Gamma_n\) has no isolated vertex: the sole white vertex has a blue neighbor which immediately forces it. The full vertex set is also zero forcing, and there are no zero forcing sets smaller than \(N-2\). Therefore
\[
\mathcal Z(\Gamma_n;x)
=
z(\Gamma_n;N-2)x^{N-2}
+
Nx^{N-1}
+
x^N,
\]
with the coefficient in degree \(N-2\) given by (4) or (5).

## Verification

The accompanying `verify.py` constructs \(D_{2n}\) from the presentation, computes the center and the noncommuting graph directly, constructs the rank-two real symmetric witness, and checks its complete off-diagonal pattern.

For
\[
3\le n\le8,
\]
the verifier also exhaustively enumerates every vertex subset whenever the graph has at most \(14\) vertices. It confirms the zero forcing number, the number of minimum zero forcing sets, and the fact that the zero forcing polynomial has exactly the three claimed terms.

Exact replay output:

```text
n=3: |V|=5, Z=3, min_sets=6, polynomial_terms={3: 6, 4: 5, 5: 1}, rank_witness=2
n=4: |V|=6, Z=4, min_sets=12, polynomial_terms={4: 12, 5: 6, 6: 1}, rank_witness=2
n=5: |V|=9, Z=7, min_sets=20, polynomial_terms={7: 20, 8: 9, 9: 1}, rank_witness=2
n=6: |V|=10, Z=8, min_sets=36, polynomial_terms={8: 36, 9: 10, 10: 1}, rank_witness=2
n=7: |V|=13, Z=11, min_sets=42, polynomial_terms={11: 42, 12: 13, 13: 1}, rank_witness=2
n=8: |V|=14, Z=12, min_sets=72, polynomial_terms={12: 72, 13: 14, 14: 1}, rank_witness=2
VERIFY_OK
```

The finite calculations are corroborative only. The theorem for arbitrary \(n\) follows from the explicit group-theoretic decomposition, the rank-two matrix constructions, and the complete two-white-vertex forcing classification.

## Relationship to prior work

Abdollahi, Akbari, and Maimani introduced the modern finite-group noncommuting graph framework and studied connectivity, diameter, girth, Hamiltonicity, domination, and structural reconstruction questions. Their article was available online on 24 March 2006. Full-text searches of the inspected source found no occurrence of “zero forcing,” “minimum rank,” or “nullity.”

Talebi studied the noncommuting graph specifically for \(D_{2n}\), with primary Mathematics Subject Classification \(20D60\). The inspected full paper determines independence number, clique number, chromatic number, and minimum vertex-cover size. It does not contain zero-forcing or graph-minimum-rank results.

Later work on the same dihedral noncommuting graph studies detour, eccentricity, mean distance, and several matrix energies. These parameters use fixed graph matrices and do not determine the minimum rank over all real symmetric matrices with the graph pattern.

The general inequality \(M(G)\le Z(G)\) comes from the AIM Minimum Rank — Special Graphs Work Group. A general minimum-rank characterization for rank at most two can recognize the rank-two conclusion after the graph decomposition is known, but it does not provide the minimum-zero-forcing-set classification or the zero forcing polynomial derived here.

## Limitations

The theorem concerns the standard noncommuting graph on noncentral elements of the dihedral group \(D_{2n}\), \(n\ge3\).

The minimum rank is over real symmetric matrices. No claim is made for other coefficient fields.

The rank-two conclusion itself is compatible with general minimum-rank characterizations for graphs of small minimum rank. The new content emphasized here is the exact zero forcing equality together with the classification and count of all minimum zero forcing sets and the complete zero forcing polynomial.

The proof uses the conventional notation that \(D_{2n}\) has order \(2n\).

## References

1. A. Abdollahi, S. Akbari, and H. R. Maimani, “Non-commuting graph of a group,” *Journal of Algebra* 298 (2006), 468–492. DOI: 10.1016/j.jalgebra.2006.02.015. Available online 24 March 2006.
2. A. Asghar Talebi, “On the Non-Commuting Graphs of Group \(D_{2n}\),” *International Journal of Algebra* 2 (2008), 957–961.
3. S. M. S. Khasraw, I. D. Ali, and R. R. Haji, “On the non-commuting graph of dihedral group,” *Electronic Journal of Graph Theory and Applications* 8 (2020), 233–239. DOI: 10.5614/ejgta.2020.8.2.3.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
