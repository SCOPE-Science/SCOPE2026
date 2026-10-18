# Burning codes and the balance jump for one-frustration bicliques

## Finding

Let \(a,b\geq3\), let \(G=K_{a,b}\) have labeled bipartition \(A=\{u_0,\ldots,u_{a-1}\}\), \(B=\{v_0,\ldots,v_{b-1}\}\), and put \(n=a+b\). Give the single edge \(u_0v_0\) negative sign and every other edge positive sign, obtaining the signed graph \(\Gamma\). In the signed-burning dynamics of [1], encode a terminal two-colouring by the set of its green vertices. Put
\[
\mathcal E=\big\{\{u_0,v_j\}:1\leq j<b\big\}\cup
\big\{\{v_0,u_i\}:1\leq i<a\big\}.
\]
**Theorem.** The *entire* family of reachable terminal green sets is
\[
\boxed{\mathcal C_{a,b}=\{\varnothing,V\}\cup
\{\{w\},V\setminus\{w\}:w\in V\}\cup
\{e,V\setminus e:e\in\mathcal E\}.}
\]
In particular \(|\mathcal C_{a,b}|=4n-2\), and its Hamming-weight enumerator is
\[
\boxed{W_{a,b}(z)=1+nz+(n-2)z^2+(n-2)z^{n-2}+nz^{n-1}+z^n.}
\]
The enumerator depends only on \(n\), not on the two part sizes separately.

For a switching set \(U\subseteq V\), let \(\Gamma^U\) denote the signature obtained by reversing the signs of edges crossing \(U\), and let \(Y(\Gamma^U)\) be its maximum possible terminal single-colour plurality. Write \(k=|U|\), and for a vertex set \(X\) define \(\epsilon(X)=1\) if some \(e\in\mathcal E\) satisfies \(e\subseteq X\), and \(\epsilon(X)=0\) otherwise. **Every** switched plurality is explicitly determined by
\[
\boxed{Y(\Gamma^U)=n-d(U),\quad
 d(U)=\begin{cases}
 0,&k=0\text{ or }k=n,\\
 \min\{k-1-\epsilon(U),\,n-k-1-\epsilon(V\setminus U)\},&0<k<n.
 \end{cases}}
\]
The minimum plurality throughout this switching class, equivalently the covering radius \(\rho(\mathcal C_{a,b})\), has a sharp part-balance transition:
\[
\boxed{\rho(\mathcal C_{a,b})=
\begin{cases}
 \lfloor n/2\rfloor-1,&n\text{ odd or }a=b,\\
 n/2-2,&n\text{ even and }a\ne b,
\end{cases}}
\]
\[
\boxed{\min_{U\subseteq V}Y(\Gamma^U)=
\begin{cases}
 (n+3)/2,&n\text{ odd},\\
 n/2+1,&a=b,\\
 n/2+2,&n\text{ even and }a\ne b.
\end{cases}}
\]
When \(a=b\), the only covering-radius words are \(A\) and \(B\); as they induce the same signing, the uniquely least-plurality signature in the switching class has every edge negative except \(u_0v_0\), which is positive.

## Assumptions and scope

The underlying graphs are finite, undirected, simple, complete bipartite graphs with \(a,b\ge3\); vertices are labeled, and the signing has exactly one negative edge before switching. The three-vertex-per-side lower bound ensures strict majority whenever a part receives exactly one oppositely signed influence; no tie then survives into another ignition. The condition is material: for \(K_{2,3}\), direct dynamics has twenty reachable terminal colourings, whereas the displayed code construction would give eighteen. No claim is made for a smaller part size or for other switching classes.

In each round, first every unburned vertex compares the signed sum of the previously burned neighbour colours, takes its strict-majority colour if that sum is nonzero, and remains unburned after a tie; then one still-unburned vertex, if any, is ignited in a chosen colour. A burned colour never changes. Identify yellow with \(+1\), green with \(-1\), and unburned with \(0\). The process ends when every vertex is burned. This fixes the order of spreading and ignition unambiguously.

## Proof

**1. All reachable terminal colourings.** Choose the first ignition at \(x\in A\), in colour \(c\in\{+1,-1\}\); the case \(x\in B\) is symmetric. At the start of round two, every vertex in \(B\) sees the first source and therefore burns. If \(x\ne u_0\), each vertex of \(B\) receives \(c\). If \(x=u_0\), the vertex \(v_0\) receives \(-c\) and every other vertex in \(B\) receives \(c\). Since \(a\ge3\), at least one other vertex in \(A\) remains unburned and may be ignited at the end of round two, in either colour. Call it \(y\).

In round three, each vertex still unburned belongs to \(A\) and has at least three already burned neighbours in \(B\). When \(x\ne u_0\), all \(B\)-colours are \(c\), and even the possibly exceptional negative edge at \(u_0v_0\) can reverse only one of these influences. Thus its net pressure has the sign of \(c\). When \(x=u_0\), the only \(B\)-vertex of colour \(-c\) is \(v_0\), but all edges from any remaining \(A\)-vertex are positive; once again at least three neighbours with at most one opposite colour give strict pressure of sign \(c\). Consequently all vertices not ignited in rounds one or two are coloured \(c\) at the spreading phase of round three. No later ignition is possible.

For \(c=+1\), if the first source is ordinary, the only possible green set is empty or the singleton \(\{y\}\). Such a singleton can be placed at any vertex, choosing another first source in its part; the assumption that both parts contain at least three vertices guarantees this. If the first source is \(u_0\), the green set contains \(v_0\) and can additionally contain one vertex \(y\in A\setminus\{u_0\}\). If the first source is \(v_0\), it similarly contains \(u_0\) and can additionally contain \(y\in B\setminus\{v_0\}\). These are precisely the empty set, the singletons, and the pairs in \(\mathcal E\). Conversely each has an explicit choice of first source and second ignition as just described. Replacing every ignition colour by its opposite negates all pressures and complements the resulting green set, proving the claimed formula for \(\mathcal C_{a,b}\). Since \(|\mathcal E|=(a-1)+(b-1)=n-2\), and \(n\ge6\) makes the six displayed cardinality levels distinct, the cardinality and weight enumerator follow.

**2. Switching and exact individual pluralities.** For \(U\subseteq V\), define \(\phi_U(w)=-1\) when \(w\in U\), and \(+1\) otherwise. Under switching, an edge sign changes as \(\sigma^U(xy)=\phi_U(x)\sigma(xy)\phi_U(y)\). If a burning state is \(\nu\), let its transformed state be \(\nu^U(w)=\phi_U(w)\nu(w)\). At an unburned vertex \(x\), its switched influence is
\[
\sum_{y\sim x}\sigma^U(xy)\nu^U(y)
=\phi_U(x)\sum_{y\sim x}\sigma(xy)\nu(y).
\]
Therefore the sign comparison, ties, and all choices of ignitions are preserved bijectively, with ignition colours transformed by \(\phi_U\). A final state becomes all-yellow on precisely the vertices where its original green set agrees with \(U\) in membership; more precisely the switched green set is the symmetric difference \(S\triangle U\). Hence
\[
Y(\Gamma^U)=n-\min_{S\in\mathcal C_{a,b}}|U\triangle S|.
\]
For \(0<k<n\), among codewords of sizes zero, one, and two the least distance from \(U\) is \(k-1\) unless \(U\) contains a pair of \(\mathcal E\), in which case it is \(k-2\). Taking the complements of those codewords yields the corresponding distance \(n-k-1\) or \(n-k-2\) according to whether \(V\setminus U\) contains such a pair. This proves the exact formula for \(d(U)\); \(d(\varnothing)=d(V)=0\).

**3. Covering radius and balance transition.** Let \(H\) be the auxiliary graph with edge set \(\mathcal E\). It is the disjoint union of two stars with centres \(u_0,v_0\), having respectively \(b-1\) and \(a-1\) leaves. Every vertex lies in one of the stars. For any nonempty proper \(U\), the exact distance formula gives
\[
d(U)\le\min\{k-1,n-k-1\}.
\]
If \(n=2m+1\), this bounds the radius by \(m-1\). Choose \(U\) as any \(m\) of the \(n-2=2m-1\) leaves of \(H\); it contains no edge, while its complement contains both centres and at least one leaf, hence an edge. The exact formula gives \(d(U)=m-1\).

Suppose \(n=2m\) and \(a=b=m\). Taking \(U=A\) leaves every edge of \(H\) across the cut, so both indicators vanish and \(d(A)=m-1\), attaining the universal upper bound. Equality forces \(k=m\) and both \(U\) and its complement to be independent in \(H\). Since each star is connected and has at least two leaves, a proper two-colouring of the disjoint stars has one colour class of size exactly one of \(2,a,b,n-2\). For \(a=b=m\ge3\), the only colour classes of size \(m\) are exactly \(A\) and \(B\). Hence these are the only deepest words.

Finally suppose \(n=2m\), \(a\ne b\). Here \(m\ge4\). If \(k\ne m\), the universal bound is at most \(m-2\). If \(k=m\) and neither side of the cut contained an edge of \(H\), that cut would be a proper two-colouring of the two stars with class size \(m\). Its possible class sizes are \(2,a,b,n-2\), none equal to \(m\) because \(a\ne b\) and \(m\ge4\). Thus at least one side contains an \(H\)-edge, forcing \(d(U)\le m-2\). Conversely choose one edge of each star, put the first into \(U\) and the second into its complement, and distribute the remaining vertices to arrange \(|U|=m\), possible since \(2\le m\le n-2\). Both sides contain an \(H\)-edge, and the formula yields \(d(U)=m-2\). The radius and all minimum pluralities follow. When \(a=b\), the two deepest switching sets \(A\) and \(B\) are complements and therefore produce the same edge signing, with every edge negative except the distinguished edge, as stated.

## Verification

The independent standard-library script `verify.py` enumerates every reachable terminal state from the exact two-stage signed-burning rules, without using the claimed code description in its state transition engine. For all twenty part-size profiles \(3\le a,b\le6\) together with \((3,7),(7,3),(4,7),(7,4)\), it compares the full reachable set with the theorem, then checks the Hamming distance formula on all \(20{,}544\) binary switching words across those profiles. It checks the radius and the weight enumerator, as well as the exact deep-hole sets for equal part sizes. Finally it independently simulates all \(192\) switched signatures on the \(K_{3,3}\) and \(K_{3,4}\) graphs, testing the switching identity. All checks passed. Execute using `python verify.py` from the directory containing the script. No dependencies outside the Python standard library are required.

These finite checks are corroboration, not substitutes for the general proof above. The complete search beyond the tested sizes is not claimed.

## Relationship to prior work

Fallat, Gupta, Khodamoradi and Zilles [1] define the signed-burning dynamics and plurality number, prove the switching equivalence of terminal colourings (Lemma 2.3, Proposition 2.9), and interpret the minimum plurality over a switching class via the covering radius of a reachable binary code (Remark 2.10). Those general facts are credited and the required switching identity is rederived above. Their exact family results in Section 3 concern signed paths. The present new claim is the complete reachable code for the one-frustrated-edge complete bipartite class, its explicit distance law for every signing, and its covering-radius and balance classification. These results are not stated in the relevant sections of [1].

The distinction between equal and unequal part sizes is invisible to the weight enumerator, even for equal total order. For example, \(K_{4,4}\) and \(K_{3,5}\) both produce thirty-word codes with identical weight enumerators, but the covering radii are respectively \(3\) and \(2\), so their minimum switching-class pluralities are respectively \(5\) and \(6\). This is a geometric rather than a weight-distribution invariant.

## Limitations

The theorem treats only the switching class represented by one negative edge on \(K_{a,b}\) for \(a,b\ge3\). It does not determine other frustration patterns, thinner complete bipartite graphs, signed-burning number, or asymptotics for general signed networks. Published-equivalence risk remains: no literature search proves uniqueness, and independent external mathematical review has not yet occurred. The cited 2026 source supplies a general code viewpoint, but not this specialized code computation. Computational verification is finite and the source-to-result comparison is limited to accessible indexed literature and the primary text inspected.

## References

[1] S. Fallat, H. Gupta, K. Khodamoradi and S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1 (first publicly posted 2026-10-01), https://arxiv.org/abs/2610.02506v1 ; full manuscript https://arxiv.org/pdf/2610.02506v1 . Particularly Definition 2.1, Lemma 2.3, Proposition 2.9, Remark 2.10 and Section 3.
