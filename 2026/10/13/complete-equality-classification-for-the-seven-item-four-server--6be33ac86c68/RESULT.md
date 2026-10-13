# Complete equality classification for the seven-item four-server three-retrieval combinatorial batch code
## Finding
A \(t=1\) combinatorial batch code with \(n=7\) items on \(m=4\) servers and retrieval requirement \(k=3\) is represented by a multiset \(\mathcal F\) of seven nonempty subsets of \(\{1,2,3,4\}\). The retrieval condition is the Hall condition that every submultiset of \(r\le 3\) items has union of size at least \(r\).

The known optimum is \(N(7,3,4)=12\). The complete equality layer consists of exactly \(46\) multisets on labeled servers. Under relabeling of the four servers these split into exactly four orbits, of sizes \(4,12,6,24\), with stabilizer orders \(6,2,4,1\). Representatives are
\[
\begin{aligned}
A&=\{\{1\},\{2\},\{3\},\{1,4\},\{2,4\},\{3,4\},\{1,2,3\}\},\\
B&=\{\{1\},\{2\},\{3\},\{1,4\},\{2,4\},\{3,4\},\{1,2,4\}\},\\
C&=\{\{1\},\{2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}\},\\
D&=\{\{1\},\{2\},\{1,3\},\{1,4\},\{2,3\},\{3,4\},\{3,4\}\}.
\end{aligned}
\]
Thus, up to relabeling both items and servers, there are exactly four optimal codes. With all seven items labeled as well as all four servers, there are exactly \(171360\) optimal incidence assignments.

## Assumptions and scope
Items are distinct requests, but two distinct items may be stored on the same subset of servers. Servers are the four labeled points \(1,2,3,4\). Retrieval is the standard combinatorial-batch-code condition with \(t=1\): any three distinct items can be assigned to three distinct servers that store them. By Hall's theorem this is equivalent to requiring every one-, two-, or three-item submultiset to have a union of at least its cardinality.

The classification is only for \((n,k,m,t)=(7,3,4,1)\). It does not assert a classification for larger parameters, erasure variants, multiset-query batch codes, or coded rather than combinatorial storage.

## Proof
Write \(a_j\) for the number of items stored on exactly \(j\) servers. For each two-server set \(U\), at most two items can have their complete storage set inside \(U\); otherwise three such items would violate Hall. Summing this inequality over all six choices of \(U\) gives
\[
3a_1+a_2\le 12.
\]
Since \(a_1+a_2+a_3+a_4=7\), if the excess storage over one copy per item is
\[
E=a_2+2a_3+3a_4,
\]
then \(2E\ge 2a_2+3a_3+3a_4\ge 9\). Hence \(E\ge 5\) and total storage is at least \(7+5=12\). The four displayed representatives satisfy Hall, so the lower bound is attained. This also independently reproduces the published value \(N(7,3,4)=12\).

At equality, subtracting twice the item-count equation from the storage equation gives
\[
a_1=a_3+2a_4+2.
\]
Singleton items must occupy distinct servers, so \(a_1\le 4\). The only arithmetically possible profiles are
\[
(a_1,a_2,a_3,a_4)\in\{(2,5,0,0),(3,3,1,0),(4,1,2,0),(4,2,0,1)\}.
\]
The last two are impossible: four singleton items occupy all four servers, and then every two-server item together with the two singleton items at its endpoints gives three items whose union has size two. Thus only the first two profiles survive.

For profile \((3,3,1,0)\), relabel so the singleton items are \(\{1\},\{2\},\{3\}\), leaving server \(4\). A two-server item contained in \(\{1,2,3\}\) would violate Hall together with its endpoint singletons, so all three two-server items must contain server \(4\). No such pair may repeat, because two copies of \(\{i,4\}\) together with \(\{i\}\) have union size two. Hence the pairs are exactly \(\{1,4\},\{2,4\},\{3,4\}\). The remaining three-server item is arbitrary. Under the stabilizer of the singleton triple there are two cases: the triple omits server \(4\), giving type \(A\), or contains server \(4\), giving type \(B\). These yield respectively \(4\) and \(12\) labeled-server multisets.

For profile \((2,5,0,0)\), relabel the singleton items as \(\{1\},\{2\}\). The pair \(\{1,2\}\) is forbidden. A pair incident with server \(1\) or \(2\) cannot repeat, because two copies together with the corresponding singleton violate Hall. Therefore only \(\{3,4\}\) may repeat, and it has multiplicity at most two. With five pair items there are exactly two possibilities: all five allowed pair types appear once, giving type \(C\); or \(\{3,4\}\) appears twice and one of the four cross pairs is omitted, giving type \(D\). These yield \(6\) and \(24\) labeled-server multisets.

The total is \(4+12+6+24=46\). Types \(A,B,C\) have seven distinct storage sets, whereas type \(D\) has one duplicated pair. Hence the number with item labels fixed is
\[
(4+12+6)\,7!+24\,\frac{7!}{2!}=171360.
\]

## Verification
The supplied verifier enumerates all \(\binom{21}{7}=116280\) multisets of seven nonempty subsets of a four-element server set. It implements Hall's condition in two independent forms: direct unions over all one-, two-, and three-item selections, and a containment-count test over one- and two-server subsets. The two predicates agree on the entire ambient census.

The exhaustive search finds minimum storage \(12\) and exactly \(46\) minimizers. A separately generated union of the four structural families is exactly the same set of \(46\) minimizers. The server-permutation action gives orbit sizes \(4,12,6,24\), and direct multiplicity accounting gives \(171360\) fully labeled incidence assignments. The replay output begins with `VERIFY_OK` and records these counts.

## Relationship to prior work
Paterson, Stinson and Wei introduced the combinatorial specialization and the Hall-type storage problem. Bujtás and Tuza later determined \(N(n,3,m)\) for all parameters; their formula specializes to \(N(7,3,4)=12\). Thus the optimum value \(12\) is prior work and is not claimed as new.

Brualdi, Kiernan, Meyer and Schroeder classified optimal combinatorial batch codes for the adjacent regimes \(n=m+1\) and \(n=m+2\). Their full text explicitly develops those two cases. For \(m=4\), the present parameter \(n=7=m+3\) lies just beyond that classification. The inspected full text of Bujtás and Tuza proves the optimal value for \(k=3\) but does not state the four equality types, the count \(46\), or the fully labeled count \(171360\). Targeted exact-parameter searches likewise found no source implying this complete equality census.

## Limitations
This is a finite equality classification at one parameter point. The exhaustive certificate is complete for the stated finite universe but does not imply a general classification for \(n=m+3\), nor does it address coded batch codes or failure-tolerant variants. Originality searches cannot exclude every obscure or unindexed thesis or table; the principal residual risk is an unpublished or poorly indexed finite census of this same parameter.

## References
1. M. B. Paterson, D. R. Stinson and R. Wei, *Combinatorial batch codes*, Cryptology ePrint Archive 2008/306; received 2008-07-08; later Advances in Mathematics of Communications 3 (2009), 13-27, doi:10.3934/amc.2009.3.13.
2. R. A. Brualdi, K. P. Kiernan, S. A. Meyer and M. W. Schroeder, *Combinatorial batch codes and transversal matroids*, Advances in Mathematics of Communications 4 (2010), 419-431, doi:10.3934/amc.2010.4.419.
3. C. Bujtás and Z. Tuza, *Optimal batch codes: Many items or low retrieval requirement*, Advances in Mathematics of Communications 5 (2011), 529-541, doi:10.3934/amc.2011.5.529.
4. Y. Ishai, E. Kushilevitz, R. Ostrovsky and A. Sahai, *Batch codes and their applications*, STOC 2004, 262-271, doi:10.1145/1007352.1007396.
