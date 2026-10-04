# Collision-layer asymptotics for tuple orbits of universal homogeneous hypergraphs
## Finding
Fix an integer \(r\ge 2\). Let \(\Gamma_r\) be the countable universal homogeneous \(r\)-uniform hypergraph and let \(G_r=\operatorname{Aut}(\Gamma_r)\). Write \(I_r(n)\) for the number of \(G_r\)-orbits on injective ordered \(n\)-tuples and \(T_r(n)\) for the number of orbits on all ordered \(n\)-tuples. Then
\[
\boxed{I_r(n)=2^{\binom nr}},\qquad
\boxed{T_r(n)=\sum_{k=0}^{n}S(n,k)\,2^{\binom kr}},
\]
where \(S(n,k)\) is a Stirling number of the second kind.

More sharply, put
\[
D_{r,j}(n)=\binom nr-\binom{n-j}{r}.
\]
For every fixed nonnegative integer \(m\), as \(n\to\infty\),
\[
\boxed{
\frac{T_r(n)}{I_r(n)}
=\sum_{j=0}^{m}S(n,n-j)\,2^{-D_{r,j}(n)}
+O\!\left(n^{2m+2}2^{-D_{r,m+1}(n)}\right).
}
\]
Thus repeated coordinates are asymptotically organized into successive collision layers. The first nontrivial layer gives
\[
\boxed{
\frac{T_r(n)}{I_r(n)}
=1+\binom n2\,2^{-\binom{n-1}{r-1}}
+O\!\left(
 n^4 2^{-\binom{n-1}{r-1}-\binom{n-2}{r-1}}
\right).
}
\]
Equivalently,
\[
\boxed{
\frac{I_r(n)}{T_r(n)}
=1-\binom n2\,2^{-\binom{n-1}{r-1}}
+O\!\left(
 n^4 2^{-\binom{n-1}{r-1}-\binom{n-2}{r-1}}
\right).
}
\]
So the injective-orbit fraction tends to one extremely rapidly, and the exact scale of the deficit records the relation arity \(r\).

For \(r=2\), the unrestricted profile begins
\[
1,1,3,15,127,1895,53071,2953575,337064047,\ldots,
\]
which is OEIS A335390. That database entry already records the exact Stirling transform and the weaker asymptotic \(T_2(n)\sim 2^{\binom n2}\). The contribution here is the homogeneous-structure interpretation, the all-\(r\) formulation, and especially the collision-layer expansion with its sharp first correction.

## Assumptions and scope
An \(r\)-uniform hypergraph is taken to have a symmetric irreflexive \(r\)-ary edge relation. The structure \(\Gamma_r\) is the Fraïssé limit of all finite \(r\)-uniform hypergraphs. Simon Thomas calls this the countable universal homogeneous \(r\)-hypergraph. It is also a basic example of a free homogeneous structure in a finite relational language, the setting treated by Siniora and Solecki.

Siniora--Solecki was first public on 2017-05-04 and its classifications include 03C15 and 03C13. Thomas's older paper is supporting prior literature for the standard universal homogeneous hypergraph itself.

## Proof
For an injective ordered tuple \((x_1,\ldots,x_n)\), its induced labeled structure is an arbitrary \(r\)-uniform hypergraph on the label set \([n]\). There are \(2^{\binom nr}\) choices. By ultrahomogeneity, two injective tuples are in the same \(G_r\)-orbit exactly when these labeled induced hypergraphs agree. Hence \(I_r(n)=2^{\binom nr}\).

For an arbitrary ordered \(n\)-tuple, first record its equality partition. If that partition has \(k\) blocks, there are \(S(n,k)\) possible equality patterns. Ordering the blocks canonically by their least tuple positions turns the distinct tuple values into an injective ordered \(k\)-tuple. Its induced hypergraph contributes \(2^{\binom kr}\) possibilities. This proves the exact Stirling transform for \(T_r(n)\).

Now set \(j=n-k\). Dividing by \(I_r(n)\) gives the exact collision decomposition
\[
\frac{T_r(n)}{I_r(n)}
=\sum_{j=0}^{n}S(n,n-j)2^{-D_{r,j}(n)}.
\]
Also
\[
D_{r,j}(n)=\sum_{t=0}^{j-1}\binom{n-t-1}{r-1}.
\]
A partition of \([n]\) into \(n-j\) blocks can be obtained from the singleton partition by \(j\) successive block mergers. Encoding each merger by a pair of labels gives the crude but sufficient bound
\[
S(n,n-j)\le \binom n2^j\le n^{2j}.
\]
Fix \(m\). For \(m+2\le j\le n/2\), every additional term in \(D_{r,j}(n)-D_{r,m+1}(n)\) is at least a positive constant times \(n^{r-1}\). Hence, after factoring out
\[
n^{2m+2}2^{-D_{r,m+1}(n)},
\]
the remaining upper bounds form a geometric tail with ratio at most \(n^2 2^{-c_r n^{r-1}}=o(1)\).

For \(j>n/2\),
\[
D_{r,j}(n)\ge \binom nr-\binom{\lceil n/2\rceil}{r}=\Theta(n^r),
\]
while the total number of set partitions is at most \(n^n=2^{O(n\log n)}\). Since \(r\ge2\), this far tail is exponentially smaller than the stated error term. This proves the fixed-depth expansion.

Taking \(m=1\), using \(S(n,n-1)=\binom n2\), and the identities
\[
D_{r,1}(n)=\binom{n-1}{r-1},\qquad
D_{r,2}(n)=\binom{n-1}{r-1}+\binom{n-2}{r-1},
\]
gives the displayed first-correction formula. Inverting \(1+\delta+O(E)\), with \(\delta^2=O(E)\) here, gives the injective-fraction statement.

## Verification
The companion standard-library verifier computes Stirling numbers independently by recurrence and by enumerating restricted-growth strings. For \(2\le r\le5\) and small \(n\), it checks the exact equality-pattern/hypergraph count against the stated transform. For \(r=2\) it reproduces the published initial A335390 row
\[
1,1,3,15,127,1895,53071,2953575,337064047.
\]
It then checks the exact collision-layer decomposition as a rational identity and numerically normalizes the total noninjective contribution by
\[
\binom n2 2^{-\binom{n-1}{r-1}}.
\]
For \(r=2\) the normalized values at \(n=12,18,24,32,40\) are approximately
\[
1.0258901,\ 1.0009980,\ 1.0000293,\ 1.0000002,\ 1.0000000013,
\]
and for higher \(r\) convergence is much faster. The replay ends with `VERIFY_OK`.

## Relationship to prior work
Thomas's 1996 paper explicitly works with the countable universal homogeneous \(k\)-hypergraph and its reducts. Siniora--Solecki treat free homogeneous structures over finite relational languages and provide a modern model-theoretic source for this family.

The exact \(r=2\) unrestricted sequence is prior: OEIS A335390 states
\[
T_2(n)=\sum_k S(n,k)2^{\binom k2}
\]
and records \(T_2(n)\sim2^{\binom n2}\). OEIS A006125 supplies the labeled-graph sequence \(2^{\binom n2}\). Accordingly, neither that exact graph-case transform nor its leading equivalence is claimed as new.

Targeted searches for random or universal homogeneous hypergraphs together with ordered tuple orbits, Stirling transforms, collision asymptotics, the factor \(2^{-\binom{n-1}{r-1}}\), and A335390 did not locate the fixed-depth expansion or the sharp first correction. published-finding corpus searches likewise returned nearby tuple-orbit results for random-poset reducts, random bipartite reducts, and the random distributive lattice, but no matching hypergraph result.

## Limitations
The exact orbit formulas are short consequences of ultrahomogeneity and equality partitions, and the asymptotic expansion uses elementary bounds. Unindexed folklore is therefore a real priority risk. The claim of originality is limited to the explicit homogeneous-hypergraph interpretation and collision-layer asymptotics, not the graph-case sequence A335390 or the standard definition of the random hypergraph. The finite replay checks formulas and numerical convergence but does not replace the asymptotic proof.

## References
1. D. Siniora and S. Solecki, “Coherent extension of partial automorphisms, free amalgamation, and automorphism groups,” arXiv:1705.01888, first submitted 4 May 2017; Journal of Symbolic Logic 85 (2020), 199–223, DOI 10.1017/jsl.2019.32.
2. S. Thomas, “Reducts of random hypergraphs,” Annals of Pure and Applied Logic 80 (1996), 165–193, DOI 10.1016/0168-0072(95)00061-5.
3. OEIS A335390, “\(a(n)=\sum_{k=0}^n S(n,k)2^{\binom k2}\).”
4. OEIS A006125, number of simple labeled graphs on \(n\) nodes, \(2^{\binom n2}\).
