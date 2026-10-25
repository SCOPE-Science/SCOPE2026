# Three-layer Poisson law and first-order convergence for random S4 reachability frames

## Finding
Let \(t\in\mathbb R\) be fixed. Sample a random directed graph \(G_n\) on \(\{1,\dots,n\}\), with no loops and each ordered edge \((u,v)\), \(u\ne v\), independently present with probability \(p_n=(\log n+t)/n\). Here \(n\) is sufficiently large that \(p_n\in[0,1]\). Write \(R_n\) for directed reachability including length-zero paths, hence a reflexive transitive relation and an \(\mathsf{S4}\) Kripke frame.

**Theorem (canonical preorder, Poisson exceptional layers, and first-order convergence).** As \(n\to\infty\), with probability \(1-o(1)\), simultaneously for all worlds \(u,v\),
\[
 uR_nv\quad\Longleftrightarrow\quad u=v\ \lor\bigl(d^+_{G_n}(u)>0\ \land\ d^-_{G_n}(v)>0\bigr).
\tag{1}
\]
Let \(I_n=\{v:d^-_{G_n}(v)=0\}\), \(O_n=\{v:d^+_{G_n}(v)=0\}\) and \(M_n=[n]\setminus(I_n\cup O_n)\). The sets \(I_n,O_n\) are disjoint with probability \(1-o(1)\); then (1) says that every element of \(I_n\) reaches every element of \(M_n\cup O_n\), all elements of \(M_n\) reach one another and every element of \(O_n\), and distinct elements within \(I_n\), respectively \(O_n\), are incomparable. The middle set is one strong component of cardinality \(n-O_{\mathrm P}(1)\). Jointly,
\[
 (|I_n|,|O_n|)\ \xrightarrow{\ d\ }\ (X,Y),\qquad
 X,Y\text{ independent }\operatorname{Poisson}(\lambda),\qquad \lambda=e^{-t}.
\tag{2}
\]
In particular, with probability \(1-o(1)\), the full automorphism group of \(([n],R_n)\) is \(S_{|I_n|}\times S_{|M_n|}\times S_{|O_n|}\).

Let \(F_{i,m,j}\) denote the reflexive preorder on disjoint sets of sizes \(i,m,j\), with identical mutual accessibility on its middle set, arrows from every initial element to all middle and final elements and from every middle element to all final elements, and no further nonreflexive arrows. For any first-order sentence \(\varphi\) in the signature with one binary relation \(R\), the finite-frame probabilities converge to
\[
 \lim_{n\to\infty}\Pr\bigl(([n],R_n)\models\varphi\bigr)
 =e^{-2\lambda}\sum_{i=0}^{\infty}\sum_{j=0}^{\infty}
 \frac{\lambda^{i+j}}{i!j!}\,\varepsilon_\varphi(i,j),
\tag{3}
\]
where \(\varepsilon_\varphi(i,j)=\lim_{m\to\infty}\mathbf1[F_{i,m,j}\models\varphi]\) is an eventually constant value in \(\{0,1\}\). Thus these random finite \(\mathsf{S4}\) frames admit an explicit first-order convergence law, generally with nontrivial limits strictly between zero and one.

## Assumptions and scope
The graph is directed and all \(n(n-1)\) possible nonloop arcs are mutually independent. The reachability relation includes reflexivity, regardless of loops in the sampled graph. The parameter \(t\) is fixed as \(n\to\infty\); no assertion is made for moving \(t\), nonindependent arcs, arbitrary random preorders, or other probability windows. The first-order language has only equality and the binary relation \(R\), without naming the original arcs, colours, or the sample labels. The structural assertions hold with probability tending to one, not for every sampled graph.

## Proof
**1. A uniform half-reachability estimate.** Let \(\operatorname{Reach}(v)\) be the set reachable from \(v\) using paths of nonnegative length, and \(\operatorname{Pre}(v)\) the analogous predecessor set. We claim with probability \(1-o(1)\):
\[
 d^+(v)>0\implies |\operatorname{Reach}(v)|>n/2,
 \qquad d^-(v)>0\implies |\operatorname{Pre}(v)|>n/2,
\tag{4}
\]
for every \(v\) simultaneously. If a vertex of positive outdegree has \(|\operatorname{Reach}(v)|=s\in[2,\lfloor n/2\rfloor]\), its reachable set \(S\) is outgoing-edge closed and contains a directed spanning out-arborescence rooted at \(v\). For a fixed labelled \(s\)-element \(S\), there are at most \(s^{s-1}\) choices of rooted directed spanning trees (Cayley's formula, with a root choice). All \(s-1\) tree arcs must be present, and all \(s(n-s)\) arcs from \(S\) to its complement absent, independently. Therefore, writing \(q_n=1-p_n\),
\[
\begin{split}
 \Pr(\exists v:\ 2\le |\operatorname{Reach}(v)|\le n/2)
 &\le\sum_{s=2}^{\lfloor n/2\rfloor}\binom ns s^{s-1}p_n^{s-1}q_n^{s(n-s)}\\
 &\le\sum_{s=2}^{\lfloor n/2\rfloor}\frac1{sp_n}
 \bigl(e n p_n e^{-p_n(n-s)}\bigr)^s=o(1).
\end{split}
\tag{5}
\]
For \(2\le s\le n/4\), the quantity in parentheses is at most \(C_t(\log n)n^{-3/4}\), so this part is \(O((\log n)/\sqrt n)\). For \(n/4<s\le n/2\), it is at most \(C_t(\log n)n^{-1/2}\), and the geometric tail beyond \(n/4\) is superpolynomially small. This establishes the first assertion of (4). Edge reversal proves the second by the same bound.

**2. Exact global reachability and the three layers.** On (4), if \(d^+(u)>0\) and \(d^-(v)>0\), the two subsets \(\operatorname{Reach}(u)\) and \(\operatorname{Pre}(v)\) each have strictly more than \(n/2\) members and hence intersect. A point of intersection supplies a directed walk from \(u\) to \(v\), proving \(uR_nv\). Conversely, a nontrivial directed path from \(u\) to \(v\) entails \(d^+(u)>0\) and \(d^-(v)>0\). This proves (1) without any assumption about independence among reachability events. The expected number of vertices with both degrees zero is \(nq_n^{2(n-1)}=O(1/n)\), so there are none with probability tending to one. Formula (1) now gives the asserted three-layer preorder and single central strong component, once (2) supplies \(O_{\mathrm P}(1)\) exceptional vertices.

**3. Joint Poisson convergence.** For fixed integers \(a,b\ge0\), choose ordered distinct vertices whose indegrees vanish (\(a\) vertices) and another disjoint ordered set whose outdegrees vanish (\(b\) vertices). The forbidden arcs total exactly \((a+b)(n-1)-ab\): the arcs from the second set into the first were counted twice. Their contribution to the mixed factorial moment \(\mathbb E[(|I_n|)_a(|O_n|)_b]\) is
\[
 (n)_{a+b}q_n^{(a+b)(n-1)-ab}\longrightarrow \lambda^{a+b}.
\tag{6}
\]
Choices in which the two designated sets overlap in \(r\ge1\) vertices number \(O(n^{a+b-r})\), while their combined zero-degree probability is \(O(n^{-a-b})\); their total is \(O(n^{-r})\). Thus all mixed factorial moments converge to those of independent \(\operatorname{Poisson}(\lambda)\) variables. The standard multivariate method of moments gives (2), including tightness of \(|I_n|+|O_n|\).

**4. First-order convergence.** On the canonical event, conditional on \((|I_n|,|O_n|)=(i,j)\) and disjointness, the relation is isomorphic to \(F_{i,n-i-j,j}\). For a sentence \(\varphi\) of quantifier rank \(q\), duplicator wins the length-\(q\) Ehrenfeucht–Fraïssé game between \(F_{i,m,j}\) and \(F_{i,m',j}\) whenever both middle cardinalities are at least \(q+1\): permanently match the two fixed initial and final layers bijectively, and respond to each previously unselected middle point with a new middle point. Distinctness and every relation atom are preserved, so the truth indicator stabilizes, defining \(\varepsilon_\varphi(i,j)\). Restrict the exceptional counts to \(i+j\le K\), use joint convergence (2) and the stabilization for sufficiently large \(n\), and then let \(K\to\infty\) using tightness. This proves (3).

**5. Automorphisms.** On the same event, the three layer types are intrinsic: initial vertices have no distinct strict predecessors, final vertices no distinct strict successors, and middle vertices belong to the unique large nontrivial mutual-accessibility class. For sufficiently large \(n\), \(M_n\) has at least two elements, so no automorphism interchanges types. Every permutation within a layer preserves the relation, proving the direct-product statement.

## Verification
The accompanying stand-alone file `verify_three_layer.py` uses only Python's standard library. It enumerates every loop-free directed graph through four worlds, computes reflexive transitive closure independently, and checks that the half-reachability condition implies the canonical formula (1). For the same exhaustive samples, it checks exact first and mixed degree-zero moments against independent formulas. It then performs reproducible seeded simulations at \(n\in\{20,40,80\}\) at \(t=0\). These checks validate finite combinatorial consequences; they do not substitute for the uniform first-moment estimate, mixed Poisson convergence or the Ehrenfeucht–Fraïssé argument. The code prints `THREE_LAYER_PREORDER_CHECK_OK` on success.

## Relationship to prior work
Zantedeschi [1] studies automorphism orbits and modal exchangeability on general Kripke frames; its full HTML text defines centered stabilizers and treats \(\mathsf{S4}\) orbit structure, but does not sample Erdős–Rényi graphs or derive Poisson-decorated random reachability preorders. Karp [2] studies the transitive closure of random directed graphs, with its accessible abstract emphasizing \(np\to c>1\) constant and a giant strong component; the complete 1990 paper was not accessible for material comparison and its possible coverage of the near-connectivity window remains a genuine risk. Pittel and Poole [3] investigate giant-component Gaussian statistics in the fixed \(np\to c>1\) sparse regime; their accessible full text was read for the model, hypotheses and results, not only the title. Bal et al. [4] study the hitting time of rainbow arborescences in an edge-coloured random directed graph process and derive ordinary directed spanning-arborescence threshold consequences;  those special probabilities are **not** claimed novel here. The new assertion assessed is the exact all-pairs canonical \(\mathsf{S4}\) preorder, joint exceptional-layer law, full first-order limiting probabilities, and associated automorphism structure, rather than a single known spanning-arborescence event.

## Limitations
No independent external audit has been performed. The closest historical full text of Karp [2] was not inspected in full; a stronger general historical reachability theorem could subsume this result. The quantitative error in the first-order mixture is not optimized, no local model with prescribed valuations is analyzed, and the critical window uses fixed \(t\). The product-group conclusion is for unlabeled relational automorphisms of \(R_n\), not automorphisms of the original sampled arc relation. The finite checker is not an infinite proof.

## References
[1] Daniel Zantedeschi, *Modal Exchangeability: Centered Symmetry and the Credal Architecture of Kripke Frames*, arXiv:2603.27547v1 (publicly posted 29 March 2026), full HTML revision arXiv:2603.27547v2, https://arxiv.org/html/2603.27547v2.

[2] Richard M. Karp, *The Transitive Closure of a Random Digraph*, Random Structures & Algorithms 1 (1990), 73–93, doi:10.1002/rsa.3240010106. Only public abstract materially available in the present comparison.

[3] Boris Pittel and Daniel Poole, *Asymptotic Distribution of the Numbers of Vertices and Arcs of the Giant Strong Component in Sparse Random Digraphs*, arXiv:1405.4022 (2014), https://arxiv.org/abs/1405.4022.

[4] A. Bal and collaborators, *Rainbow arborescence in random digraphs*, arXiv:1411.3364 (2014), https://arxiv.org/abs/1411.3364.