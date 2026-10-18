# Closure-map envelopes and unique reconstruction of finite-chain IS4 frames
## Finding

Consider the ordered chain \(C_n=\{0<1<\cdots<n-1\}\), with \(n\ge1\). A **birelational IS4 frame on the chain** is a reflexive and transitive relation \(R\subseteq C_n\times C_n\) satisfying two confluence properties: 

\[
(i\le i'\ \&\ iRj)\ \Longrightarrow\ \exists j'\ge j\;(i'Rj') \quad\text{(forth-up)},
\]
\[
(iRj\ \&\ j\le j')\ \Longrightarrow\ \exists i'\ge i\;(i'Rj')\quad\text{(back-up)}.
\]

Write \(h(i)=\max\{j:iRj\}\) and \(b(j)=\max\{i:iRj\}\). Then \(h,b:C_n\to C_n\) are order-preserving, extensive, idempotent maps (closure operators). **Every ordered pair of such closure operators occurs.** More precisely, put
\[
U(h,b)=\{(i,j):j\le h(i)\text{ and }i\le b(j)\},
\]
\[
L(h,b)=\operatorname{RTC}\big(\{(i,h(i)):i\in C_n\}\cup\{(b(j),j):j\in C_n\}\big),
\]
where \(\operatorname{RTC}\) is reflexive transitive closure. Both \(L(h,b)\) and \(U(h,b)\) are birelational IS4 frames with the stipulated exact row and column maxima, and **all** frames with maxima \((h,b)\) are precisely the reflexive transitive relations \(R\) with \(L(h,b)\subseteq R\subseteq U(h,b)\). Thus there are exactly \(4^{n-1}\) realizable ordered extrema profiles.

There is a sharp criterion for when these extrema determine the **entire** relation, rather than an interval of possible relations. For \(0\le t\le n-2\), let \(H_t=1\) if \(h(t)>t\), otherwise \(0\); define \(B_t\) analogously for \(b\). Then \(L(h,b)=U(h,b)\) if and only if, for every \(1\le t\le n-2\), neither
\[
(H_{t-1},H_t,B_t)=(1,1,0)
\qquad\text{nor}\qquad
(B_{t-1},B_t,H_t)=(1,1,0)
\]
occurs. The number \(Q_n\) of uniquely reconstructible ordered profiles therefore satisfies
\[
\boxed{Q_1=1,\qquad Q_n=4\cdot3^{n-2}\ (n\ge2).}
\]

In particular, all four profiles are unique at \(n=2\), whereas exactly twelve of the sixteen profiles are unique at \(n=3\). For \(n\ge2\), the fraction of profiles determining a unique frame is \((3/4)^{n-2}\).

## Assumptions and scope

The source-frame definition is the finite, **infallible** birelational intuitionistic-S4 frame (a bi-preorder) with both forth-up and back-up interaction conditions, not an arbitrary relation and not one satisfying only one confluence property. The order \(\le\) is the fixed total order on the labelled set \(C_n\). There is no assertion about predicate valuations, frame validity equivalence, or general finite posets. Relations may have non-symmetric modal edges; reflexivity and transitivity are taken for the modal accessibility relation \(R\), not only for \(\le\).

For a reflexive relation, the row and column maxima always exist. An extensive order-preserving idempotent self-map of \(C_n\) sends each point to the least fixed point not below it; its fixed-point set includes \(n-1\). Conversely any subset of \(C_n\) containing \(n-1\) determines a unique such closure operator. All extrema profiles here are *ordered* pairs \((h,b)\), i.e., row- and column-maxima data are not identified under reversal or converse.

## Proof

**1. Extrema become closure operators.** Fix an IS4 relation \(R\). If \(i\le i'\), the edge \(iRh(i)\) and forth-up give an edge \(i'Rj'\) with \(j'\ge h(i)\), hence \(h(i')\ge h(i)\). Similarly, back-up gives \(b(j')\ge b(j)\) whenever \(j\le j'\). Reflexivity implies \(h(i)\ge i\) and \(b(j)\ge j\). Since \(iRh(i)\) and \(h(i)Rh(h(i))\), transitivity yields \(iRh(h(i))\), whence \(h(h(i))\le h(i)\); extensivity yields the reverse inequality. Dually, \(b(b(j))\le b(j)\) follows by chaining \(b(b(j))Rb(j)\) with \(b(j)Rj\). Therefore \(h,b\) are closure operators.

**2. Canonical extremal relations.** Conversely take any two closure operators \(h,b\). The relation \(U=U(h,b)\) is reflexive because \(h(i),b(i)\ge i\). For transitivity, suppose \(iUj\) and \(jUk\). Then \(j\le h(i)\) and \(k\le h(j)\), so monotonicity and idempotence give \(k\le h(j)\le h(h(i))=h(i)\). Also \(i\le b(j)\) and \(j\le b(k)\), hence \(i\le b(j)\le b(b(k))=b(k)\). Thus \(iUk\).

The forced edge \((i,h(i))\) lies in \(U\) because \(i\le h(i)\le b(h(i))\). The forced edge \((b(j),j)\) lies in \(U\) because \(j\le b(j)\le h(b(j))\). Thus the reflexive transitive closure \(L\) of the forced edges lies inside the transitive \(U\). For either \(L\) or \(U\), every edge in row \(i\) ends at most at \(h(i)\), while its forced edge reaches \(h(i)\); likewise every column \(j\) has exact maximum \(b(j)\). The same is true for every intermediate relation. Conversely any relation with the given extrema contains the forced edges and is contained in \(U\), so if it is reflexive/transitive it contains \(L\). Finally, for *any* relation on a finite chain with nonempty rows/columns, forth-up is equivalent to nondecreasing row maxima, and back-up to nondecreasing column maxima: apply the required witness to the largest element of the relevant row/column; conversely that largest element itself supplies each witness. Hence \(L,U\), and every reflexive-transitive intermediate relation, satisfy both confluence axioms. Each pair \((h,b)\) occurs at least once.

**3. Local characterization of unique reconstruction.** For a closure operator \(h\), its fibres are consecutive intervals \([a,c]\), ending at a fixed point \(c\); its indicator \(H_t\) is one precisely when \(t\) is not a fixed point. Similarly for \(b\) and \(B\). For \(i<j\), the condition \(iUj\) is equivalent to \(i,j\) lying in the same \(h\)-fibre: the column inequality \(i\le b(j)\) is automatic and the row inequality is \(j\le h(i)\). Dually, for \(i>j\), \(iUj\) holds precisely when \(i,j\) lie in the same \(b\)-fibre.

If \(H_{t-1}=H_t=1\) and \(B_t=0\), then \((t-1,t)\in U\): the consecutive points lie inside an \(h\)-fibre. This edge does not lie in \(L\). Indeed \(h(t)>t\) means \(t\) is not a fixed point or image of \(h\), so no generating forward edge terminates at \(t\); and \(b(t)=t\) means no nontrivial generating backward edge terminates at \(t\). The last step of any nontrivial \(L\)-path into \(t\) would have to be such an edge. If \(B_{t-1}=B_t=1\) and \(H_t=0\), then \((t,t-1)\in U\) but not in \(L\): no nontrivial backward generator leaves \(t\) (since \(t\) is not an image of \(b\)) and no nontrivial forward generator leaves \(t\) (since \(h(t)=t\)). Thus either forbidden pattern prevents uniqueness.

Now assume neither forbidden pattern occurs. Consider an upward edge \(iUj\) with \(i<j\), inside an \(h\)-fibre \([a,c]\). Since \(iLh(i)\) is a forced edge, if \(j=c\) the edge is already in \(L\). Otherwise \(j<c\), so this fibre has at least three elements. For each \(q\in[a+1,c-1]\) we have \(H_{q-1}=H_q=1\); absence of the first forbidden pattern forces \(B_q=1\). If \(c<n-1\), then \(H_c=0\), and since \(B_{c-1}=1\), absence of the second forbidden pattern forces \(B_c=0\). If \(c=n-1\), the endpoint is automatically fixed by \(b\). In either case, every interior \(q\) of the \(h\)-fibre has \(b(q)=c\). Therefore the forced edges \(i\to c\) and \(c=b(j)\to j\) yield \(iLj\). For a downward edge \(iUj\), \(i>j\), use the symmetric argument on the containing \(b\)-fibre \([a,c]\): if \(i=c\) the backward edge \(c\to j\) is forced; otherwise absence of the second pattern forces \(H_q=1\) in the interior and absence of the first forces \(H_c=0\), so \(h(i)=c\); the forced edges \(i\to c\to j\) witness \(iLj\). Diagonal edges are reflexive. Hence \(U\subseteq L\), proving equivalence.

**4. Counting.** There are \(2^{n-1}\) closure operators, one per choice of the \(n-1\) nonfinal fixed-point bits. Thus there are \(4^{n-1}\) ordered profiles. For the uniqueness count, read the paired indicator symbols \((H_t,B_t)\) left to right from the four-letter alphabet \(00,10,01,11\). The only forbidden adjacent transitions are \(10\to10\), \(01\to01\), \(11\to10\), and \(11\to01\). With one symbol, the counts ending in \(00,10,01,11\) are \((1,1,1,1)\). For two symbols they are \((4,2,2,4)\), and this last vector is taken by the transition matrix to exactly three times itself. Induction yields a total \(4\cdot3^{m-1}\) admissible strings of length \(m=n-1\), for \(m\ge1\). For \(n=1\), the empty string determines the sole profile. This establishes the count and its sharp boundary.

## Verification

Run `python verify_is4_profiles.py` using Python 3 and its standard library. The checker tests the original quantified frame axioms directly on all reflexive binary relations with up to four worlds, without reducing to extrema. It independently lists all closure-operator pairs through eight worlds, constructs both proposed canonical relations, compares exact extrema, checks transitivity and the confluence axioms, and tests the local iff criterion. For sizes up to six it enumerates all intermediate reflexive transitive relations and checks them against the original axioms. Counts of arbitrary IS4 relations for chain sizes one through six are \(1,4,20,126,1026,11324\); these figures are **checks** rather than an asserted general formula. The unique-profile counts through eight worlds are \(1,4,12,36,108,324,972,2916\). The script terminates with `VERIFY_OK`.

These finite checks do not replace the quantified proof for arbitrary \(n\).

## Relationship to prior work

Girlando, Kuznets, Marin, and Straßburger's 2026 work establishes proof-theoretic decidability and finite models for intuitionistic modal \(\mathsf{IS4}\) and \(\mathsf{IK4}\); its published abstract motivated a finite semantic reconstruction question, but its full manuscript was not accessible during this investigation. Balbiani, Diéguez, Fernández-Duque, and McLean establish constructive \(\mathsf{S4}\) birelational frame classes and the precise forth-up/back-up interaction principles (their Definitions 7 and 8). Becker, Das, Marin, and Padhiar use these same two interaction properties for intuitionistic tense relations.

The closest independently indexed mathematical finding, *Maxima normal form and exact census for chain birelational relations*, characterizes the two confluence conditions on a chain by nondecreasing row/column maxima **without** imposing reflexivity or transitivity, and gives a reconstruction interval with *independently optional* entries. Here reflexivity and transitivity force both extrema to be idempotent closure operators, require the lower reconstruction to be **transitively closed**, and make intermediate entries dependent. The main new claim is the complete closure-map envelope, the sharp local iff criterion for uniqueness, and its \(4\cdot3^{n-2}\) census; none follows as a stated numerical result from the unrestricted binary-relation census. Separate KI logic work uses row minima and maxima under a different confluence pairing, and upward-flat Heyting--Lewis chain results produce a Bell-number census under different axioms.

Searches for equivalent closure-map pairs, transitive Fischer--Servi relations, exact uniqueness profiles, ordered relation envelopes, and the specific count found no direct earlier statement. This is a bounded best-knowledge originality assessment, not a proof of absolute publication uniqueness.

## Limitations

The theorem requires a finite **chain** and a reflexive/transitive modal relation satisfying both displayed confluence properties. It does not count all such relations in a closed formula, merely their distinct extrema profiles and those that uniquely specify the relation. The resulting bounds need not extend to partial orders, nontransitive intuitionistic-modal relations, or frames with uninhabited/exceptional worlds. An unindexed semigroup-theoretic or order-theoretic equivalent enumeration could predate this investigation. The 2026 motivating paper's full text was not verified; the 2024 frame paper's Definitions 7--8 and adjacent discussion were materially inspected.

## References

[1] Marianna Girlando, Roman Kuznets, Sonia Marin, and Lutz Straßburger, *A decision procedure for intuitionistic modal logic IS4 (and IK4)*, arXiv:2609.24922, first public version September 21, 2026.

[2] Philippe Balbiani, Martín Diéguez, David Fernández-Duque, and Brett McLean, *Constructive S4 modal logics with the finite birelational frame property*, arXiv:2403.00201, first public version 2024; Definitions 7 and 8.

[3] Justus Becker, Anupam Das, Sonia Marin, and Paaras Padhiar, *The proof theory and semantics of second-order (intuitionistic) tense logic*, arXiv:2602.06253, first public version February 5, 2026.

[4] *Maxima normal form and exact census for chain birelational relations*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-maxima-normal-form-and-exact-census-for-chain-birelational-relat--f1e0f9b64170.
