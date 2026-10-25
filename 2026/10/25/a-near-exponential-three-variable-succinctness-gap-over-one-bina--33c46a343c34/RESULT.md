# A near-exponential three-variable succinctness gap over one binary relation

## Finding
For every integer \(k\geq1\), there is an explicitly constructible first-order formula \(\psi_k(x,y)\) using **only three variable names, equality, Boolean connectives, quantifiers, and one binary relation symbol** \(R\). Its ordinary syntax-tree size \(s_k\) is \(O(k\log(k+1))\). Put \(r=2k\), \(t=\lceil\log_2 r\rceil\), let \(b_j(i)\in\{0,1\}\) be the \(j\)-th bit of the length-\(t\) binary expansion of \(i\), for \(0\leq i<r\) and \(1\leq j\leq t\), and set
\[
M_k=1+r(t+1)+\sum_{i=0}^{r-1}\sum_{j=1}^{t}b_j(i)\leq 1+r(2t+1).
\]
Every calculus-of-relations (CoR) circuit \(C\) equivalent to \(\psi_k\) **on all finite directed graphs, loops allowed**, satisfies the composition-gate lower bound
\[
\boxed{\quad g_{;}(C)\geq \frac{2^{k-1}}{M_k^3}.\quad}
\]
In particular, a family of single-binary-relation \(\mathrm{FO}^{3}\) formulas of size \(s\) requires \(2^{\Omega(s/\log(s+2))}\) CoR circuit composition gates, even with arbitrary sharing and Boolean operations. This is a **near-exponential** gap, not the unresolved fully exponential \(2^{\Omega(s)}\) gap for a fixed vocabulary.

## Assumptions and scope
A *finite directed graph* is a finite nonempty set with an arbitrary binary relation \(R\), possibly asymmetric and with loops. A CoR circuit is a finite acyclic directed graph with input relation \(R\), constants \(0,1,I\) (empty, universal, identity), the Boolean operations, converse, and relational composition \(X;Y\), interpreted over the complete square of its finite domain. The gate count \(g_{;}\) counts distinct composition gates only: Boolean and converse gates are free, and common subexpressions may be shared. Thus the statement covers, in particular, the ordinary CoR language of the cited source. Formulas have at most the two free variables \(x,y\); size counts occurrences in a syntax tree, not the number of shared abbreviation definitions. Equality is available as in ordinary first-order logic.

The essential known input is Uezato's Theorem 1.3: for every \(k\geq1\), every CoR circuit over \(2k\) independent binary symbols computing
\[
\Phi_k(x,y)=\exists z\,\bigwedge_{h=0}^{k-1}\left[
 (S_{2h}(x,z)\wedge S_{2h}(z,y))\vee
 (S_{2h+1}(x,z)\wedge S_{2h+1}(z,y))
\right]
\]
on all finite relational structures has at least \(2^{k-1}\) composition gates. The present proof reduces this published lower bound to the signature containing only \(R\).

## Proof
**1. A bit-coded one-relation interpretation.** Fix arbitrary \(2k\) binary relations \(S_0,\ldots,S_{r-1}\) on a finite nonempty set \(A\). Introduce \(M_k\) tags: one root \(\rho\); layers \(\ell_{i,j}\) for \(0\leq i<r\), \(1\leq j\leq t+1\); and a marker \(m_{i,j}\) only where \(b_j(i)=1\). The encoded domain is \(U=A\times T\). Its *only* \(R\)-edges are as follows, with all \(a,b\in A\):

- Root loops \((a,\rho)R(a,\rho)\), and marker loops \((a,m_{i,j})R(a,m_{i,j})\).
- The entry edges \((a,\rho)R(a,\ell_{i,1})\) for each \(i\).
- The identity-propagation edges \((a,\ell_{i,j})R(a,\ell_{i,j+1})\) for \(1\leq j<t\).
- The data edges \((a,\ell_{i,t})R(b,\ell_{i,t+1})\) precisely when \((a,b)\in S_i\).
- The exit edges \((b,\ell_{i,t+1})R(b,\rho)\).
- Bit-marker edges \((a,\ell_{i,j})R(a,m_{i,j})\) whenever \(b_j(i)=1\).

No layer vertex has a self-loop, and a marker has no edge to a distinct vertex. Therefore the one-variable test
\[
D(v):=R(v,v)\land\exists w\,(R(v,w)\land w\ne v)
\]
selects precisely the roots, while on a layer the test
\[
B(v):=\exists w\,(R(v,w)\land R(w,w)\land w\ne v)
\]
recognizes precisely whether that layer has its marker. In particular, \(B(a,\ell_{i,j})\) holds iff \(b_j(i)=1\) for \(j\leq t\). For each \(i\), define \(T_i(u,v)\) to assert \(D(u)\land D(v)\) and the existence of a directed path of **exactly \(t+2\) edges** from \(u\) to \(v\), with every internal vertex loop-free and with its vertices at positions \(1,\ldots,t\) satisfying \(B\) or \(\neg B\) according to the bits \(b_1(i),\ldots,b_t(i)\). The last internal vertex (position \(t+1\)) needs only the loop-free test.

This path test has a direct \(\mathrm{FO}^{3}\) expression of size \(O(t)\). To see this without relying on extra variable names, keep one endpoint as the final variable; traverse the path in a nested chain of existential quantifiers that alternately **rebind the two other names**. At a newly quantified intermediate vertex, conjoin the required loop test and bit test before entering the next nested quantifier. The bit test \(B(v)\) is implemented in an inner scope using one of the two temporarily available variable names (and then its scope closes), so it does not increase the total set of three names. Each path edge and each guard contributes \(O(1)\) syntax nodes. Renaming bound variables gives variants with any ordered pair from \(\{x,y,z\}\) as free endpoints.

A loop-free internal vertex cannot be a root or marker. From a root its first loop-free successor is a layer \(\ell_{i,1}\). A path between two roots through exactly \(t+1\) loop-free internal vertices can neither switch gadgets nor visit an extra root, so it follows a single tag string \(\ell_{j,1},\ldots,\ell_{j,t+1}\). Its recorded length-\(t\) bit string uniquely determines \(j=i\). The only non-identity step is the edge from \(\ell_{i,t}\) to \(\ell_{i,t+1}\), so, for every \(a,b\in A\),
\[
\boxed{T_i((a,\rho),(b,\rho))\ \Longleftrightarrow\ (a,b)\in S_i.}
\]
Notice that marker loops and root loops do not produce spurious successful paths, because *every internal vertex* must be loop-free.

**2. The three-variable formula.** Substitute the tests \(T_i\) in the published hard formula:
\[
\psi_k(x,y):=D(x)\land D(y)\land\exists z\Bigl(D(z)\land
\bigwedge_{h=0}^{k-1}
\bigl[(T_{2h}(x,z)\land T_{2h}(z,y))\lor
(T_{2h+1}(x,z)\land T_{2h+1}(z,y))\bigr]\Bigr).
\]
Each \(T_i\) has exactly its displayed two free variables and uses only the three names \(x,y,z\), rebinding its scratch name internally. Every occurrence has syntax-tree size \(O(t)\), including the expanded tests \(D,B\); hence \(s_k=O(kt)=O(k\log(k+1))\). By the boxed path identity, on all encoded structures
\[
\psi_k((a,\rho),(b,\rho))\ \Longleftrightarrow\ \Phi_k(a,b).
\]

**3. Simulating any one-relation CoR circuit blockwise.** Let \(C\) be any CoR circuit using the single symbol \(R\) and computing \(\psi_k\) on every finite graph. For each circuit gate \(G\) on \(U=A\times T\), define its \((u,v)\) *tag block*, for \(u,v\in T\), by
\[
G_{uv}:=\{(a,b)\in A^2:((a,u),(b,v))\in G\}.
\]
All input blocks of \(R\) are among \(S_0,\ldots,S_{r-1}\), identity \(I_A\), or the empty relation, as the edge specification shows. Blocks of universal \(1_U\) are \(A^2\); blocks of identity \(I_U\) are \(I_A\) when \(u=v\), otherwise empty. Complement is complement inside \(A^2\), Boolean operations act componentwise, and converse transposes and exchanges the tag indices. Most importantly, the exact composition rule is
\[
(G;H)_{uv}=\bigcup_{w\in T}\bigl(G_{uw};H_{wv}\bigr).
\]
Therefore each original composition gate can be simulated by **at most \(M_k^3\) composition gates total** across all \(M_k^2\) output blocks, followed by free unions. The translations of all blocks of previously built gates are shared; arbitrary Boolean/converse gates introduce *no* additional composition gates. By induction through the acyclic circuit, there is a CoR circuit \(C^{\flat}\) over \(S_0,\ldots,S_{r-1}\) computing the root-root block of \(C\) and satisfying
\[
g_{;}(C^{\flat})\leq M_k^3g_{;}(C).
\]
Because \(C\) is equivalent to \(\psi_k\) on **all** finite single-relation graphs, it agrees in particular on every encoded graph constructed from an arbitrary finite \(S_0,\ldots,S_{r-1}\)-structure. The identity in step 2 implies \(C^{\flat}\equiv_{\mathrm{fin}}\Phi_k\). Uezato's Theorem 1.3 now yields
\[
2^{k-1}\leq g_{;}(C^{\flat})\leq M_k^3g_{;}(C),
\]
which proves the displayed lower bound. Finally \(M_k=O(k\log(k+1))\) and \(s_k=O(k\log(k+1))\). Inverting this size relation along the constructed family gives \(k=\Omega(s_k/\log(s_k+2))\), so the polynomial denominator in \(M_k\) does not change the near-exponential exponent. \(\square\)

## Verification
A standalone pure-Python finite checker, `fixed_signature_gap_checker.py`, reproduces the tag encoding for sample vocabularies, checks the root and bit detection, tests the exact coded-path recovery against the original relations, and compares each induced block-circuit operation to direct one-relation evaluation for complement, transpose, Boolean operations and composition. The executed output was `FIXED_SIGNATURE_CODE_AND_BLOCK_SIMULATION_OK 640`. The computational tests cover finite samples; they do not establish the unrestricted circuit lower bound or replace the published source theorem.

## Relationship to prior work
Uezato [1] proves an exponential \(\mathrm{FO}^{3}\)-to-CoR composition-gate lower bound for formulas with \(2k\) **independent** binary relation symbols (Theorem 1.3), explicitly noting in Remark 4.1 that the fully exponential lower bound over a fixed vocabulary is unknown. The present construction uses that theorem without changing it: binary-labelled layer paths compress the symbols into one binary relation at logarithmic formula length per symbol, and the tag-block identity controls how one-relation CoR *circuits* translate back with polynomial composition-gate overhead. The result establishes a near-exponential lower bound over one symbol; it does **not** establish the conjectured fully exponential fixed-vocabulary bound, and it does not preserve the positivity or single-quantifier form of the original family. General signature encodings by graph gadgets, and matrix/block simulations, are recognized existing techniques; the distinctive scientific claim is their precise combination with the three-variable definability and **composition-gate** lower bound in this setting.

## Limitations
The lower bound assumes equivalence over **all finite graphs**, not only finite graphs of a particular cardinality or any restricted graph class. It does not give a lower bound for every formula, an exponential \(2^{\Omega(s)}\) bound, or a bound for positive three-variable formulas on one symbol. The proof imports the published exponential lower-bound theorem as an explicit premise; it does not independently re-prove that source theorem. An earlier unlocated equivalent fixed-signature coding argument could affect historical priority. No independent scientific audit has been performed.

## References
[1] Yuya Uezato, *An Exponential Succinctness Gap between Three-Variable Logic and the Calculus of Relations*, arXiv:2609.26778v1, first public 2026-09-22, Theorem 1.3, Remark 4.1. https://arxiv.org/abs/2609.26778

[2] Mathematical Reviews, *Mathematics Subject Classification 2020*, entry 03B10 (classical first-order logic). https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=03B38
