# Exact Lucas-number shortest cyclic covers of binary words with runs at most two

## Finding
For each integer \(k\ge 3\), let \(\mathcal R_k\) be the set of all length-\(k\) binary words that contain neither `000` nor `111` as a factor. Define \(C_k\) as the minimum number of symbols in a cyclic binary word whose cyclic length-\(k\) factors include **every** element of \(\mathcal R_k\). Candidate cyclic words may repeat required factors and may, a priori, contain forbidden factors.

Let \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and \(L_k=F_{k-1}+F_{k+1}\) (Lucas numbers). Then

\[
\boxed{\;|\mathcal R_k|=2F_{k+1},\qquad C_k=2L_k-2,\qquad C_k-|\mathcal R_k|=2(F_{k-1}-1).\;}
\]

Moreover, **some optimal cyclic host itself avoids `000` and `111` across the cyclic boundary.** The repetition overhead satisfies

\[
\lim_{k\to\infty}\frac{C_k-|\mathcal R_k|}{|\mathcal R_k|}=\frac{3-\sqrt5}{2}.
\]

For \(k=3,4,5,6,7,8,9,10\), the exact covering lengths are \(6,12,20,34,56,92,150,244\). This is a shortest-cover theorem, not a universal-cycle/no-repetition assertion.

## Assumptions and scope
Words use \(\{0,1\}\); a **run** is a maximal constant block. The language \(\mathcal R_k\) has all runs of length at most two. A length-\(N\) cyclic host is understood through periodic extension, with exactly \(N\) cyclic windows of each fixed length. The theorem applies to all integers \(k\ge3\), with no requirement of equal symbol frequencies or primitive period, and allows unrestricted host windows in the optimization. The primary classification is MSC2020 68R15.

## Proof
Put \(n=k-1\). Consider the full binary de Bruijn directed graph on all length-\(n\) vertices, with an edge labeled \(e=e_0\cdots e_{n}\) from its length-\(n\) prefix to its length-\(n\) suffix. Regard the members of \(\mathcal R_k\) as compulsory edges. Let \(G\) be their subgraph, supported on vertices avoiding `000` and `111`. For a supported vertex \(v\), its incoming required-edge degree is one when its first two symbols agree and two otherwise; its outgoing degree is one when its last two agree and two otherwise. Thus the required-edge deficits \(D\) are exactly the admissible length-\(n\) words **beginning with unequal letters and ending with equal letters**. The surpluses \(P\) begin with equal letters and end with unequal letters. Every degree discrepancy has magnitude one, and vertices outside the support are balanced with zero required degree.

For \(v\in D\), let \(t(v)\) be the position (zero-based) of its **first equal adjacent pair**: \(v_{t(v)}=v_{t(v)+1}\). Since its first pair is unequal and its last pair is equal, \(1\le t(v)\le n-2\). A path of \(j<t(v)\) edges in the *unrestricted* de Bruijn graph shifts away the first \(j\) symbols, so the destination still begins with the unequal pair \(v_jv_{j+1}\). It therefore cannot be in \(P\). Consequently, every path from \(v\) to any surplus has length at least \(t(v)\); this lower bound explicitly permits intermediate forbidden windows.

For any cyclic host covering every compulsory edge, subtract one copy of every required edge from the multiset of its traversed edges. The remaining edge multiset has divergence \(+1\) at each vertex of \(D\), divergence \(-1\) at each vertex of \(P\), and zero elsewhere. Standard integral flow decomposition expresses those extra edges as source-to-sink paths from each deficit to a surplus, plus directed cycles. Thus the number of added edges is at least \(\sum_{v\in D}t(v)\), even for unrestricted hosts.

To attain the bound, write \(v=x s\) where \(|x|=t(v)\) and \(s=v_{t(v)}\cdots v_{n-1}\). The prefix \(x\) is alternating, \(s\) starts in an equal pair, and \(s\) ends in an equal pair. Append to \(s\) the unique alternating string \(y\) of length \(t(v)\) whose first letter differs from the last letter of \(s\). Put \(\Phi(v)=s y\). This word lies in \(P\): it avoids both forbidden triples, begins in an equal pair and ends in an unequal pair.

The map \(\Phi:D\longrightarrow P\) is a bijection. Indeed, for \(w\in P\), locate its **last** equal adjacent pair. The prefix through that pair is \(s\), and the remainder is the alternating suffix \(y\), necessarily starting opposite the last letter of \(s\). Let \(t=|y|\); there is exactly one alternating word \(x\) of length \(t\) ending in the letter opposite \(s_0\), and then \(xs\in D\) has first equal pair at index \(t\) and maps to \(w\). This is the inverse construction. Hence every surplus is used exactly once.

For each \(v\), shift through its length-\(t(v)\) alternating suffix extension \(y\). This gives a directed path of exactly \(t(v)\) edges from \(v\) to \(\Phi(v)\). It stays entirely in the run-two language, since \(v\) was admissible and every appended symbol is opposite the preceding one. Add all these paths to \(G\). The resulting directed multigraph is balanced. The original run-two graph \(G\) is strongly connected: between any two admissible vertices, append a sufficiently long alternating bridge beginning opposite the last source symbol and ending opposite the first target symbol, then append the target word. Both bridge parities can be obtained by selecting its length. Therefore the balanced multigraph is connected and has an Eulerian circuit. Its edge-label word is a cyclic host covering every member of \(\mathcal R_k\), with no forbidden triple, and with exactly \(\sum t(v)\) extra windows. This proves equality of the unrestricted and constructed optima.

It remains to evaluate the sum. For \(m\ge2\), let \(h_m\) count admissible length-\(m\) words beginning with a specified doubled letter and ending in an equal pair. The first bit determines all succeeding run symbols; every run has length one or two. Here \(h_2=1\), \(h_3=0\), and for \(m\ge4\), the first and last runs have length two, while the intervening \(m-4\) positions decompose into runs of sizes one or two. Hence \(h_m=F_{m-3}\) for \(m\ge4\). A deficit whose first equal pair begins at index \(t\) has an alternating prefix followed by a length-\(n-t\) suffix beginning and ending with double letters. There are exactly \(2h_{n-t}\) such deficits. Therefore

\[
\sum_{v\in D}t(v)=2\sum_{m=2}^{n-1}(n-m)h_m=2(F_n-1).
\]

The final identity follows by induction: the sum is zero for \(n=2\), and its increase when \(n\) advances by one is \(\sum_{m=2}^{n-1}h_m=F_{n-2}\). Since a length-\(k\) allowed word is specified by its initial bit and a composition of \(k\) into run lengths one and two, \(|\mathcal R_k|=2F_{k+1}\). Substituting \(n=k-1\) proves the stated Lucas formula. The ratio limit follows from \(F_{k-1}/F_{k+1}\to(3-\sqrt5)/2\).

## Verification
The accompanying standalone Python 3 program `verify.py` independently generates all run-two words, balances the de Bruijn multigraph using the explicit bijection, constructs an Eulerian cycle and checks every required cyclic window. It covers all orders \(3\le k\le18\). A separate pure-Python Hungarian assignment computes unrestricted shortest-path matching costs for \(3\le k\le11\), while direct exhaustive enumeration rules out shorter hosts for \(3\le k\le5\). Successful run marker:

`VERIFY_OK exact_Lucas_cycles_k=3..18 independent_assignment_k=3..11 exhaustive_hosts_k=3..5`

All tests are finite corroboration; the proof above establishes the infinite theorem.

## Relationship to prior work
The de Bruijn graph/Eulerian method is classical. Moreno and Matamala (arXiv:0711.1695) address de Bruijn sequences in forbidden-factor languages via Eulerian-cycle selection. Leitner and Godbole (arXiv:0808.1309) study universal cycles for several restricted word classes. Compeau, Pevzner and Tesler (2011) explain how multiset edge traversals and Eulerian circuits model circular sequence reconstruction. Those tools are not asserted to be original here. In contrast to a universal cycle, the present graph has nonzero degree imbalances for every \(k\ge4\) and must repeat some required windows. Its **exact unrestricted minimum length**, explicit balanced duplication, and Lucas evaluation are the claims under review. Related single-forbidden-pattern cyclic-cover formulas do not imply the two-simultaneous-forbidden-pattern result by deletion or symmetry.

## Limitations
The result concerns binary words with exactly the two forbidden triples `000` and `111`; it does not classify all minimum hosts or extend automatically to larger maximum run lengths, different alphabets, or arbitrary forbidden sets. No claim of novelty certification or independent audit is made. A differently phrased covering theorem in inaccessible or unindexed sources could overlap; the closest 2004/2007 and 2008 papers were available only through metadata/abstracts in this inspection, and a later run-length-limited de Bruijn paper addresses a different maximal distinct-window objective but could contain further comparisons.

## References
1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (public 2007-11-12), https://arxiv.org/abs/0711.1695.
2. A. Leitner and A. P. Godbole, *Universal Cycles of Restricted Classes of Words*, arXiv:0808.1309 (public 2008-08-08), https://arxiv.org/abs/0808.1309.
3. P. E. C. Compeau, P. A. Pevzner and G. Tesler, *How to apply de Bruijn graphs to genome assembly*, Nature Biotechnology 29 (2011), 987–991, https://pmc.ncbi.nlm.nih.gov/articles/PMC5531759/.
4. Y. M. Chee, D. T. Dao, T. L. Nguyen, D. H. Ta and V. K. Vu, *Run Length Limited de Bruijn Sequences for Quantum Communications*, ISIT (2022), https://doi.org/10.1109/ISIT50566.2022.9834795. (Later related work, not the date-defining source.)
