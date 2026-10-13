# Minimum row counts for ternary three-key Armstrong relations

## Finding
Let \(\mu(n)\) be the least number of **distinct rows** in a table of length \(n\) over an alphabet of at most three symbols per column such that its minimal keys are exactly the \(3\)-element subsets of the columns. Equivalently, distinct rows agree in at most two columns, and every pair of columns is exactly the agreement set of at least one pair of rows.

For every admissible \(n\geq3\), the exact minimum is
\[
\mu(3)=4,\qquad \mu(4)=4,\qquad \mu(5)=6,\qquad
\mu(6)=7,\qquad \mu(7)=7.
\]
There is no such ternary table with \(n\geq8\), by the previously known theorem \(f(3,3)=7\) of Chee, Zhang and Zhang. The new content is the complete minimum-row profile, particularly the strict gaps \(\mu(5)>5\) and \(\mu(6)>6\).

## Assumptions and scope
A row is a word in \(\{0,1,2\}^n\); each column may use fewer than three symbols. Coordinate permutations and independent symbol renamings do not change the defining property. An agreement set of distinct rows \(u,v\) is \(A(u,v)=\{j:u_j=v_j\}\). The exact requirement is \(|A(u,v)|\le2\) for all distinct \(u,v\), and for every two-element subset \(J\subseteq\{1,\ldots,n\}\) there exist distinct rows with \(A(u,v)=J\). All inequalities are over finite sets of **distinct** rows.

## Proof
**General counting lower bound.** A pair of rows witnesses at most one pair of columns, because its agreement set has size at most two. Every pair of columns needs a witness. Therefore \(\binom{m}{2}\ge\binom{n}{2}\) in an \(m\)-row instance, giving \(m\ge n\) for \(n\ge3\). In particular, \(m<n\) is excluded without computation.

**The diagonal obstruction.** Suppose \(m=n\). Equality of the two binomial coefficients forces a bijection between row pairs and column pairs: every row pair agrees in exactly two columns, and every column pair has exactly one witnessing row pair. Regard a column as a partition of the \(m\) rows into at most three nonempty symbol classes. Encode it by an edge mask \(E\) on \(\binom{m}{2}\) row pairs, with an edge when the rows have equal symbols. The diagonal equality demands a family of \(m\) distinct masks satisfying, for any two masks \(E_i,E_j\), \(|E_i\cap E_j|=1\), and no edge of the complete row-pair graph belongs to three masks.

All column partitions, modulo independent symbol relabeling, are generated once by restricted-growth strings: begin with label zero and permit the next label to be at most one larger than the maximum previous label, with labels at most two. An all-equal column is impossible in a diagonal instance with \(m\ge3\): any other two columns must share some witness, which would then occur in at least three columns. Removing the all-equal partition leaves precisely \(4\), \(40\), and \(121\) candidate masks for \(m=3,5,6\), respectively.

Perform an increasing-index depth-first traversal of candidate mask families. At each extension, require one shared edge with each previously selected mask and forbid any edge occurring in three masks. This search enumerates **every** possible diagonal witness under independent symbol relabelings and column permutations. It produces no family of size \(m\) for \(m\in\{3,5,6\}\). The Python verifier's counts of visited search nodes, including the root, at successive depths are
\[
\begin{array}{c|rrrrrrr}
m&0&1&2&3&4&5&6\\\hline
3&1&4&0&0&0&0&0\\
5&1&40&402&988&276&0&0\\
6&1&121&3131&22980&32769&2462&0
\end{array}
\]
These zeros, combined with the general lower bound, establish \(\mu(3)\ge4\), \(\mu(5)\ge6\), and \(\mu(6)\ge7\). The standalone C++ program independently generates canonical partitions and performs the same complete search with a different recursion order and pruning; its intermediate counts need not agree, but all three terminal counts are zero.

**Matching constructions.** The following rows are presented in order, without separators, with each digit a column value:

* Four rows, four columns: `0000`, `0011`, `0101`, `1001`.
* Six rows, five columns: `00000`, `00111`, `01012`, `02222`, `10022`, `20220`.
* Seven rows, seven columns: `3221211`, `1322121`, `1132212`, `2113221`, `1211322`, `2121132`, `2212113`.

The last instance is a known seven-row ternary construction reported by Chee, Zhang and Zhang and traces to the earlier orthogonal-double-cover example. Every listed pair of rows agrees in at most two positions, and every pair of column positions is realized as an exact agreement set; these assertions are independently checked by both programs. Deleting any one column from the four-column instance yields a valid four-row, three-column instance, and deleting any one column from the seven-column instance yields a valid seven-row, six-column instance. In each deletion, old witnesses for pairs of retained columns remain exact witnesses, and distinct rows remain distinct. Thus all five lower bounds are sharp.

## Verification
With the Python standard library, run `python3 verify_python.py`. Independently compile and execute `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp`. Both programs generate all candidate column partitions and search all permitted diagonal families; they also check the displayed finite witnesses directly, including uniqueness of rows, three-symbol restrictions, agreement-set sizes and all required column-pair witnesses. Each program reports the exact minimum-row profile \(4,4,6,7,7\).

## Relationship to prior work
Beeri, Dowd, Fagin and Statman studied minimum Armstrong-relation sizes without fixing such a small alphabet. Katona, Sali and Schewe introduced the bounded-domain coding formulation and general bounds; their \(m\ge n\) argument for \(k=3\) is compatible with, but does not determine, strictness for the cases \(n=5\) and \(n=6\). Chee, Zhang and Zhang exhibited a ternary seven-column relation and established the known maximal admissible number of columns, \(f(3,3)=7\). The present exact *minimum-row* calculation adds the two strict finite obstructions and the complete small-domain profile. The graph-theoretic formulation is connected to orthogonal double covers, as developed by Ganter, Gronau and Mullin; generic existence theorems for double covers do not impose the required partition-into-at-most-three-classes condition.

## Limitations
The finite impossibility claims use exhaustive, independently implemented enumeration, not an independent formal proof system. The result concerns only ternary alphabets and exactly-three-element minimal keys, not general key systems or other alphabet sizes. Literature comparison identified no prior exact minimum-row profile, but unindexed computations, specialized database papers, or conference appendices could contain some entries. No independent audit has been performed.

## References
1. C. Beeri, M. Dowd, R. Fagin, R. Statman, *On the Structure of Armstrong Relations for Functional Dependencies*, J. ACM 31 (1984), 30–46, DOI `10.1145/2422.322414`.
2. B. Ganter, H.-D. O. F. Gronau, R. C. Mullin, *On Orthogonal Double Covers of \(K_n\)*, Ars Combinatoria 37 (1994), 209–221, `https://combinatorialpress.com/article/ars/Volume%20037/volume-37-paper-19.pdf`.
3. G. O. H. Katona, A. Sali, K.-D. Schewe, *Codes that attain minimum distance in every possible direction*, Central European Journal of Mathematics 6 (2008), 1–11, DOI `10.2478/s11533-008-0001-4`.
4. Y. M. Chee, H. Zhang, X. Zhang, *Complexity of Dependencies in Bounded Domains, Armstrong Codes, and Generalizations*, IEEE Trans. Inform. Theory 61 (2015), 812–819, DOI `10.1109/TIT.2014.2377735`; authorized preprint `https://arxiv.org/pdf/1906.06070` (posted 2019; original conference version 2013).
