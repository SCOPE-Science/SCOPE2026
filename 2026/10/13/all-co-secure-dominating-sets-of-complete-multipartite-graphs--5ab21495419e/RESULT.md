# All co-secure dominating sets of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), and let \(V_1,\ldots,V_r\) be its partite classes. For \(S\subseteq V(G)\), put
\[
s_i=|S\cap V_i|,\qquad t_i=n_i-s_i,
\]
and let
\[
p=\bigl|\{i:s_i>0\}\bigr|.
\]

The co-secure dominating sets are exactly the following.

For \(p=1\), domination forces \(S=V_i\) for the unique occupied part. This set is co-secure if and only if
\[
n_i\ge2
\]
or there is another singleton part \(V_j\).

Suppose \(r\ge3\). If \(p=2\), every such set \(S\) is co-secure. If \(p\ge3\), then \(S\) is co-secure if and only if either \(V(G)\setminus S\) meets at least two parts, or \(V(G)\setminus S\) is one entire part. Equivalently, among sets meeting at least two parts, the only failures are
\[
S=V(G)
\]
and the sets
\[
S=V(G)\setminus T
\]
where \(T\) is a nonempty proper subset of a single part.

Suppose \(r=2\), so \(G=K_{a,b}\), and suppose \(S\) meets both parts. Then \(S\) is co-secure if and only if
\[
t_1,t_2\ge1,
\]
and
\[
s_1\ge2\ \text{or}\ t_2=1,\qquad
s_2\ge2\ \text{or}\ t_1=1.
\]

Consequently,
\[
\gamma_{cs}(G)=
\begin{cases}
1,&r\ge3\text{ and at least two parts are singletons},\\
2,&r\ge3\text{ and fewer than two parts are singletons},\\
1,&G=K_{1,1},\\
b,&G=K_{1,b},\ b\ge2,\\
\min\{a,b\},&G=K_{a,b},\ a,b\ge2.
\end{cases}
\]

There is also a closed polynomial for every multipartite graph with at least three parts. Let
\[
N=\sum_i n_i,\qquad q=\bigl|\{i:n_i=1\}\bigr|,
\]
and let \(\varepsilon_i=1\) when \(n_i\ge2\) or \(q\ge2\), and \(\varepsilon_i=0\) otherwise. Define
\[
C_{cs}(G;x)=\sum_{S\text{ co-secure dominating}}x^{|S|}.
\]
Then
\[
\boxed{
C_{cs}(G;x)=
(1+x)^N-\sum_i(1+x)^{n_i}+r-1-x^N
-\sum_i x^{N-n_i}\bigl((1+x)^{n_i}-x^{n_i}-1\bigr)
+\sum_i\varepsilon_i x^{n_i}
}.
\]

For \(K_{a,b}\), the occupancy criterion above is already an exact coefficient formula:
\[
C_{cs}(K_{a,b};x)
=
\eta_a x^a+\eta_b x^b+
\sum_{\substack{1\le s\le a-1\\1\le t\le b-1}}
\binom{a}{s}\binom{b}{t}x^{s+t}
\mathbf 1\!\left[
(s\ge2\text{ or }b-t=1)
\land
(t\ge2\text{ or }a-s=1)
\right],
\]
where \(\eta_a=1\) exactly when \(a\ge2\) or \(b=1\), and \(\eta_b=1\) exactly when \(b\ge2\) or \(a=1\).

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. A dominating set \(S\) is co-secure dominating when every \(v\in S\) has a neighbor \(u\notin S\) such that
\[
(S\setminus\{v\})\cup\{u\}
\]
is still a dominating set.

The theorem treats ordinary co-secure domination. It does not concern secure domination, secure total domination, or co-secure variants with additional connectivity or semitotal constraints.

## Proof

A set \(S\) dominates a complete multipartite graph exactly when either it meets at least two parts or it is one whole part. Indeed, if \(S\) lies in a single part but omits a vertex of that part, the omitted vertex has no neighbor in \(S\).

Fix a selected vertex \(v\in V_i\). Any permissible replacement \(u\notin S\) must lie in a different part \(V_j\), since vertices inside one part are nonadjacent.

First suppose \(S=V_i\). If \(n_i\ge2\), deleting \(v\) leaves another selected vertex in \(V_i\), and inserting any \(u\in V_j\) produces a dominating set meeting two parts. If \(n_i=1\), the swap leaves a singleton \(\{u\}\), which dominates exactly when \(V_j=\{u\}\). This proves the one-part case.

Now suppose \(r\ge3\) and \(S\) meets exactly two parts. Choose an unoccupied third part \(V_j\). Every selected vertex is adjacent to every vertex of \(V_j\). Replacing any selected vertex by any vertex of \(V_j\) leaves selected vertices in at least two parts, so the swapped set dominates. Hence every two-part-supported set is co-secure.

Suppose next that \(r\ge3\) and \(S\) meets at least three parts. Removing one selected vertex leaves selected vertices in at least two parts, regardless of whether the removed vertex was the sole selected vertex of its part. Therefore the swapped set will dominate whenever a replacement exists outside the removed vertex's part. Such a replacement fails to exist for some selected vertex exactly when the complement is empty, or when the complement is contained in a single occupied part. Thus co-security holds exactly when the complement meets at least two parts or is one entire unoccupied part. This is equivalent to the stated failure description.

Finally suppose \(r=2\), with occupied parts \(V_1,V_2\). For a selected \(v\in V_1\), a replacement must come from \(V_2\), so \(t_2\ge1\). If \(s_1\ge2\), deleting \(v\) leaves both parts occupied, and any such replacement works. If \(s_1=1\), deleting \(v\) leaves only \(V_2\) occupied; after inserting one omitted vertex of \(V_2\), the new set dominates exactly when it becomes all of \(V_2\), namely exactly when \(t_2=1\). The symmetric argument for \(V_2\) gives the bipartite criterion.

The minimum formulas follow immediately. For \(r\ge3\), either a singleton whole part is co-secure because a second singleton part exists, or two vertices in two different parts form a co-secure set. For \(K_{1,b}\) with \(b\ge2\), the singleton side cannot be co-secure and any set meeting both sides fails at the unique selected-side replacement condition, while the whole \(b\)-vertex side is co-secure. For \(K_{a,b}\) with \(a,b\ge2\), either whole part is co-secure, giving the upper bound \(\min\{a,b\}\); the bipartite criterion rules out any smaller two-part-supported set.

For \(r\ge3\), start with all subsets that meet at least two parts:
\[
(1+x)^N-\sum_i(1+x)^{n_i}+r-1.
\]
Delete \(V(G)\), contributing \(x^N\), and delete every set obtained from \(V(G)\) by removing a nonempty proper subset of one part. For part \(V_i\), these contribute
\[
x^{N-n_i}\bigl((1+x)^{n_i}-x^{n_i}-1\bigr).
\]
Finally add the co-secure one-part sets \(V_i\), producing the \(\varepsilon_i x^{n_i}\) terms. This proves the polynomial.

## Verification

The accompanying `artifacts/verify.py` constructs every nondecreasing multipartite part-size profile of total order \(2\) through \(10\). It checks every vertex subset directly from the definition: domination is tested by neighborhoods, and for every selected vertex the code searches every outside neighbor for a valid dominating swap.

Independently, the script evaluates the structural characterization above and the polynomial coefficients. It compares all three descriptions for every subset and every profile.

The replay checks \(128\) multipartite profiles and \(64{,}916\) subsets. The finite computation is corroborative only; the proof above establishes the result for arbitrary positive part sizes.

## Relationship to prior work

Cui, Li, Zhang, Chen, and Xiong study co-secure domination in a 2024 paper whose stated problems ask for structural characterizations involving the co-secure domination number. Their paper was published on December 27, 2024 and lists MSC \(05C69\). Its full accessible text develops forbidden-induced-subgraph conditions for equalities such as \(\gamma_{cs}(G)=\alpha(G)\) and \(\gamma_{cs}(G)=\gamma_s(G)\), rather than an all-set classification of complete multipartite graphs.

The foundational co-secure literature determines values for paths, cycles, and several standard families and proves general bounds. Joseph and Sangeetha's 2018 paper specifically advertises Jahangir, friendship, and helm graphs. The searched literature did not yield a complete-multipartite co-secure polynomial or the support/complement criterion proved here.

A nearby result in the current database gives the secure-domination polynomial of complete multipartite graphs. Secure domination reverses the quantifier direction: every outside vertex must be able to replace a selected defender. Co-secure domination instead requires every selected vertex to have an outside replacement. The two all-set classifications are therefore not implication-equivalent, and their multipartite support obstructions differ.

## Limitations

The theorem is specific to complete multipartite graphs. It does not provide a general algorithm for arbitrary perfect, cograph, chordal, or bipartite graphs.

The originality assessment is literature-based, not an absolute uniqueness proof. Co-secure domination has older literature under closely related terminology, and a poorly indexed source could contain a special-case formula. The directly inspected recent papers and targeted searches did not reveal a complete-multipartite all-set classification or polynomial.

## References

1. J. Cui, T. Li, J. Zhang, X. Chen, and L. Xiong, “Co-Secure Domination Number in Some Graphs,” Axioms 14 (2025), article 10, published online December 27, 2024, DOI 10.3390/axioms14010010.
2. A. Joseph and V. Sangeetha, “Bounds on Co-Secure Domination in Graphs,” International Journal of Mathematics Trends and Technology 55 (2018), 158–164, DOI 10.14445/22315373/IJMTT-V55P520.
3. S. Arumugam, K. Ebadi, and M. Manrique, “Co-secure and Secure Domination in Graphs,” Utilitas Mathematica 94 (2014), 167–182.
4. J. Cui, T. Li, X. Chen, and L. Xiong, “Characterization of Some Claw-Free Graphs in Co-Secure Domination Number,” Mathematics 13 (2025), article 2426, DOI 10.3390/math13152426.
