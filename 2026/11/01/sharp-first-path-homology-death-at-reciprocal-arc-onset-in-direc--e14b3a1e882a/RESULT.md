# Sharp first-path-homology death at reciprocal-arc onset in directed cyclic powers

## Finding
For each integer \(n\ge3\) and each \(0\le k\le n-1\), let \(D_{n,k}\) be the digraph on \(\mathbb Z/n\mathbb Z\) having all arcs \(i\longrightarrow i+j\) for \(1\le j\le k\), with residues read modulo \(n\). Use standard *regular* GLMY path homology over \(\mathbb Z\). Then
\[
H_1^{\mathrm{path}}(D_{n,k};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&1\le k<\lceil n/2\rceil,\\
0,&k=0\text{ or }\lceil n/2\rceil\le k\le n-1.
\end{cases}
\]
At every nonzero stage the class of the directed Hamiltonian cycle
\[
z_n=\sum_{i\in\mathbb Z/n\mathbb Z}(i,i+1)
\]
is an integral generator. Every inclusion \(D_{n,k}\hookrightarrow D_{n,k+1}\) before the first zero stage carries this generator to the same generator. Thus the degree-one integral persistence module has precisely the interval \([1,\lceil n/2\rceil)\), with stalk \(\mathbb Z\) and identity transition maps. Reduced degree-zero persistence has exactly \(n-1\) intervals \([0,1)\).

The sharp death scale \(\lceil n/2\rceil\) is also the first scale at which a reciprocal pair of arcs exists. At that scale, an explicit integral \(2\)-chain consisting of \(n-1\) allowed elementary two-paths has boundary \(z_n\). The result concerns low degrees only; no classification of higher path homology is asserted.

## Assumptions and scope
An allowed regular \(p\)-path is a sequence \((v_0,\dots,v_p)\) with each consecutive pair a directed arc and adjacent vertices distinct. The free abelian group of allowed paths is \(A_p\). The regular boundary deletes successive entries with alternating signs, and irregular terms (with consecutive repeated vertices) are zero. The GLMY group \(\Omega_p\subset A_p\) consists of chains whose regular boundary is allowed; in particular \(\Omega_1=A_1\). Path homology is the homology of the chain complex \((\Omega_*,\partial)\). No assumption about a field, a prime order, or the parity of \(n\) is made.

For \(k=0\), the digraph has \(n\) isolated vertices; for \(k\ge1\), it is connected because all forward unit arcs occur. All persistence intervals use the integer filtration parameter \(k\), with left-closed and right-open endpoints.

## Proof
Write \(e_{i,j}=(i,i+j)\) for \(1\le j\le k\). All indices in this proof are modulo \(n\). For \(2\le j\le k\), the regular elementary two-path \((i,i+j-1,i+j)\) has three allowed boundary edges: its successive increments are \(j-1\) and \(1\), and its shortcut has increment \(j\). Thus it is an element of \(\Omega_2\), and
\[
\partial(i,i+j-1,i+j)
=e_{i+j-1,1}-e_{i,j}+e_{i,j-1}.
\]
By iterating this equality, every allowed edge \(e_{i,j}\) differs by a two-boundary from the sum \(P(i,j)=\sum_{t=0}^{j-1}e_{i+t,1}\). This is a statement about one-chains, not an assertion that individual edges are cycles. Consequently every one-cycle is homologous to a one-cycle supported on the unit arcs. A unit-arc chain \(\sum_i c_i e_{i,1}\) is a cycle exactly when all \(c_i\) are equal, since its boundary coefficient at vertex \(i\) is \(c_{i-1}-c_i\). Therefore the class of \(z_n\) generates \(H_1\), so the only possibilities are a quotient of \(\mathbb Z\).

Suppose \(1\le k<\lceil n/2\rceil\), equivalently \(2k<n\). On the free abelian group of **all regular ordered pairs** of distinct vertices define the integer functional \(W(u,v)\) to be the positive residue of \(v-u\) in \(\{1,\dots,n-1\}\). An arbitrary elementary allowed two-path has increments \(a,b\in\{1,\dots,k\}\). Because \(a+b\le2k<n\), its endpoint pair is regular and
\[
W\bigl(\partial(i,i+a,i+a+b)\bigr)=b-(a+b)+a=0.
\]
This calculation takes place in the full regular one-chain group, so it remains valid when the shortcut \((i,i+a+b)\) is forbidden. It follows by linearity that the restriction of \(W\) to allowed one-chains annihilates \(\partial\Omega_2\). But \(W(z_n)=n\ne0\). Hence no nonzero integral multiple of \(z_n\) can be a boundary. Since \(z_n\) already generates, \(H_1\cong\mathbb Z\).

Now let \(k_* =\lceil n/2\rceil\), \(a=k_*\), and \(b=n-k_*\), so \(1\le a,b\le k_*\) and \(a+b=n\). The backtracking path \(t=(0,a,0)\) is allowed and regular (its *consecutive* vertices are different). Its middle deleted face is irregular and zero. Hence \(t\in\Omega_2\) and
\[
\partial t=e_{0,a}+e_{a,b}.
\]
For any \(u\) and \(1\le j\le k_*\), define an integral two-chain
\[
Q(u,j)=\sum_{s=2}^{j}(u,u+s-1,u+s),
\qquad\partial Q(u,j)=P(u,j)-e_{u,j};
\]
the empty sum for \(j=1\) is zero. Every term is in \(\Omega_2\) by the first paragraph. Therefore the following **explicit** chain is in \(\Omega_2\):
\[
T_n=t+Q(0,a)+Q(a,b).
\]
Its boundary telescopes to
\[
\partial T_n=P(0,a)+P(a,b)=z_n.
\]
The chain has \(1+(a-1)+(b-1)=n-1\) elementary two-path terms, counted with their displayed coefficients. This proves \(H_1=0\) at \(k=k_*\). The very same chain remains allowed at every larger scale, so \(H_1=0\) there too.

For \(k=0\), \(\Omega_1=0\), hence \(H_1=0\). For \(1\le k<k_*\), all inclusion maps preserve the literal chain \(z_n\), which is a generator at both stages. No other first-homology class or torsion can appear. The degree-one persistence statement follows, including the sharp endpoint. Finally \(D_{n,0}\) has \(n\) connected components and \(D_{n,1}\) is connected, proving the claimed reduced degree-zero barcode. The presence of a reciprocal pair is equivalent to existence of two steps \(a,b\le k\) with \(a+b=n\), which holds exactly when \(k\ge\lceil n/2\rceil\).

## Verification
The standalone `verify.py` constructs the original directed edges and all allowed regular two-paths. It forms a full generating set for \(\Omega_2\) by taking each fillable elementary two-path and all differences of two-paths sharing a forbidden endpoint pair. It computes boundary ranks independently over the four prime fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_{101}\), and checks whether adjoining the unit Hamiltonian cycle increases boundary rank. For every \(3\le n\le12\) and every \(1\le k<n\), the predicted first Betti number and survival of the cycle agree with these computations. The checker also tests the integer winding cancellation for the nonreciprocal stages and evaluates the actual integral boundary of \(T_n\) for \(3\le n\le30\). Its observed result is `VERIFY_OK low_degree_models= 65 boundary_generators= 16096 explicit_integer_fillings= 28 four_prime_fields=2,3,5,101`. These finite tests corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work
Tang and Yau, *Path Homology of Circulant Digraphs*, arXiv:2602.04140 (first public version 2026-02-04; inspected revision v2 of 2026-10-09), Theorem 3.15, **already prove** the all-field first-homology stability and inclusions for interval connection sets whenever \(n>2k\); they also prove higher-degree results in that stable range. The persistence assertion in the present result is **not claimed as new in that stable range**. The contribution here is the integral completion across the excluded boundary \(2k\ge n\), the sharp reciprocal-arc death criterion, and the explicit uniform integral filling chain, which together close the entire degree-one barcode. Their theorem has no conclusion for the boundary and post-boundary stages.

Kapulkin and Koyanagi, *Stability of Persistent Path Homology of Path Complexes*, arXiv:2607.26226, establish general stability theory but do not give this exact cyclic-power barcode. Earlier work on cyclic tournaments gives the integral generator at the special odd-order scale immediately before the reciprocal threshold; that special case is contained in both the known stable range and the present completed classification. Other published work on random directed graphs' first path homology concerns probabilistic rather than these deterministic exact parameters. No equivalent covering result was identified among the inspected sources and indexed comparisons; unindexed equivalences remain possible.

## Limitations
The theorem determines only regular GLMY path homology in degrees zero and one and their persistence for consecutively added positive steps. It does not determine higher-dimensional homology, path-homotopy groups, or arbitrary noninterval connection sets. The stable nonreciprocal calculation largely overlaps Tang and Yau's stronger existing theorem; novelty is limited to the sharp missing transition and its integral filling. Full exhaustiveness of the literature cannot be guaranteed.

## References
1. Xinxing Tang and Shing-Tung Yau, *Path Homology of Circulant Digraphs*, arXiv:2602.04140; first submitted 2026-02-04, v2 2026-10-09, especially Theorem 3.15 and Sections 3.2–3.3; https://arxiv.org/html/2602.04140v2.
2. Chris Kapulkin and Kyle Koyanagi, *Stability of Persistent Path Homology of Path Complexes*, arXiv:2607.26226, first submitted 2026-07-28; https://arxiv.org/html/2607.26226v1.
3. Thomas Chaplin, *First Betti number of the path homology of random directed graphs*, arXiv:2111.13493; original preprint 2021-11-26.
4. Shaobo Di, Sergei O. Ivanov, Lev Mukoseev, and Mengmeng Zhang, *On the path homology of Cayley digraphs and covering digraphs*, arXiv:2305.15683, first submitted 2023-05-25.
