# Sharp three-term additive coverage by distinct power values in index-one Galois rings

## Finding

Let \(R=\operatorname{GR}(p^m,p^{mf})\) have characteristic \(p^m\), residue field \(\mathbb F_q\) with \(q=p^f\), and let \(P=\{x^d:x\in R\}\setminus\{0\}\), where \(d\ge2\), \(p\nmid d\), and \(\gcd(d,q-1)=1\). A sum of three *distinct power values* means \(u+v+w=b\), with \(u,v,w\in P\) and \(u,v,w\) pairwise distinct. Then every target \(b\in R\) admits such a representation precisely in the following cases:

\[
\begin{array}{ll}
 p\text{ odd}: & q\ge7,\ \text{or }(q=5,\ m\ge2),\ \text{or }(q=3,\ m\ge3);\\
 p=2: & q\ge8,\ \text{or }(q=4,\ m\ge2),\ \text{or }(q=2,\ m>d).
\end{array}
\]

The boundary cannot be made monotone in subset size: in \(\mathbb F_5\), distinct *pairs* of nonzero elements cover the field, while distinct *triples* omit zero.

## Assumptions and scope

Here \(p\) is prime, \(f,m\) are positive integers, and the exponent \(d\) is fixed only by \(d\ge2\), \(p\nmid d\), and \(\gcd(d,q-1)=1\). We use \(\mathfrak m=pR\) for the unique maximal ideal and write \(\overline{x}\) for reduction to \(\mathbb F_q\). In particular, no bound is imposed on \(m\) or \(f\). The order of the unit group is \((q-1)q^{m-1}\). Consequently \(\gcd(d,|R^\times|)=1\), so taking \(d\)-th powers permutes \(R^\times\). Thus all units lie in \(P\). Extra nonunit powers can occur only when \(m>d\). We use only these facts about power values, not a claim that all nonzero ring elements are powers.

## Proof

**1. Large residue fields.** For any prescribed \(t\in\mathbb F_q\), seek three pairwise distinct nonzero field elements \(a,b,c\) summing to \(t\). If the characteristic is odd and \(q\ge7\), fix \(a\ne0\) and choose \(b\) outside the at-most-five-element set \(\{0,a,t-a,t-2a,(t-a)/2\}\). Then \(c=t-a-b\) is nonzero and distinct from \(a,b\). If the characteristic is two and \(q\ge8\), choose \(a\in\mathbb F_q^\times\) with \(a\ne t\), and choose \(b\) outside \(\{0,a,t-a\}\). Again \(c=t-a-b\) is nonzero and distinct from both: \(c=b\) would require \(t=a\). For any target \(B\in R\), lift \(a,b\) to arbitrary units \(u,v\in R\), and put \(w=B-u-v\). The three reductions are pairwise distinct, hence so are the lifted units. This proves coverage for every \(q\ge7\), irrespective of length.

**2. Residue field of size five.** In \(\mathbb F_5\), the sum of the four nonzero elements is zero; a triple of distinct units has sum minus the omitted nonzero element. Thus no triple has sum zero in length one, and every nonzero field target is represented. For \(m\ge2\), an arbitrary target whose reduction is nonzero lifts a triple with three distinct nonzero reductions. For a target whose reduction is zero, use residue pattern \((1,1,3)\). Pick two distinct units reducing to \(1\), possible because each residue fiber contains \(5^{m-1}\ge5\) elements; the uniquely determined third summand reduces to \(3\), so it is a distinct unit. All targets are covered.

**3. Residue field of size four.** In \(\mathbb F_4\), the three nonzero elements sum to zero, and there is no other triple of distinct nonzero elements. Thus at length one all nonzero targets fail. At \(m\ge2\), a zero-residue target lifts the triple of all three distinct nonzero reductions. Given a nonzero residue target \(t\), choose \(a\in\mathbb F_4^\times\setminus\{t\}\). The pattern \((a,a,t)\) sums to \(t\) in characteristic two. Choose two distinct lifts of \(a\) (each residue fiber has at least four elements), and solve for the third summand, whose reduction is \(t\), distinct from both.

**4. Residue field of size three.** At \(m=1\), only two nonzero power values exist. At \(m\ge2\), every target reducing to \(1\) or \(2\) is covered by respectively the patterns \((1,1,2)\) and \((1,2,2)\): choose two distinct lifts of the repeated residue and solve uniquely for the singleton. For a target \(B\in3R\), all three nonzero residues must be equal, since the only nonzero residue solutions of \(a+b+c=0\) are \((1,1,1)\) and \((2,2,2)\). At \(m=2\), \(R\cong\mathbb Z/9\mathbb Z\): each of the residue-one and residue-two fibers contains exactly three units, with respective sums \(3\) and \(6\) modulo nine. In particular zero is missing, so coverage fails. For \(m\ge3\), let \(V=3R\), of odd order \(|V|=3^{m-1}\ge9\). Fix a lift \(a\) of residue one and set \(z=B-3a\in V\). Choose \(v\in V\setminus\{0,z,z/2\}\), where \(z/2\) is uniquely defined because multiplication by two is invertible on the additive group \(V\). The lifts \(a,a+v,a+z-v\) are pairwise distinct units whose sum is \(B\). This proves the stated threshold.

**5. Residue field of size two.** Here \(R\cong\mathbb Z/2^m\mathbb Z\), the exponent \(d\) is odd, and \(d\ge3\). If \(m\le d\), every nonzero \(d\)-th power is odd. Three such values have odd sum, so no even target can occur. If \(m>d\), then \(m\ge4\), every odd residue is a \(d\)-th power, and \(2^d\in P\) is a nonzero even power. For every even \(B\), write \(B-2^d=u+v\) with distinct odd residues \(u,v\): take \(u=1\) and \(v=B-2^d-1\), unless \(v=1\); in that case take \(u=3\) instead (\(2\not\equiv6\pmod{2^m}\)). For every odd \(B\), the triple \(1,3,B-4\) consists of distinct odd residues except at \(B\equiv5,7\pmod{2^m}\); use \(1,5,B-6\) at \(B=5\), and \(3,5,B-8\) at \(B=7\). These are pairwise distinct for \(m\ge4\). The resulting unit triples and the unit-unit-nonunit triples cover all targets.

Combining the five cases proves both necessity and sufficiency with all quantified parameters.

## Verification

The companion `verify.py` independently enumerates the actual distinct power-value set and all unordered triples for selected unramified rings. It includes prime-power residue rings and extension rings of residue-field sizes four, eight, and nine, and checks exactly the predicted missing-target sets. These finite checks are diagnostics only; the proof above handles all parameters.

Execute with `python3 verify.py`. It prints `VERIFY_OK` after every assertion succeeds. The script uses integer arithmetic for Galois rings represented as quotients of polynomial rings; none of the mathematical conclusions assumes untested higher cases.

## Relationship to prior work

Zijie Gu's 2026 preprint [1] studies distinct \(n\)-subset sums of \(d\)-th-power values over all Galois rings. It proves asymptotic equidistribution for \(n\ge3\), supplies general exact character/sieve expressions and finite sufficient positivity bounds, and classifies asymptotic uniformity at \(n=2\). The present statement instead isolates the **finite, necessary-and-sufficient all-target positivity threshold for \(n=3\)** in the index-one regime; its proof requires only unit-fiber geometry and identifies small-length obstructions not expressed by the asymptotic bounds. The paper's Appendix B recalls the Li–Wan exact field formula [2], which already implicitly determines the field cases; those cases are included here only as boundaries of the ring-wide classification. Earlier papers of Ding and Zhou [3,4] treat length-two odd-characteristic Galois rings and general exact image formulas; they may implicitly yield some of the length-two instances, although the full texts could not be accessed for a decisive comparison. No independence or external priority certification is claimed.

## Limitations

The classification assumes \(\gcd(d,q-1)=1\) and \(p\nmid d\); it says nothing about proper power subgroups or higher fixed subset sizes. It is an analytic extraction and structural refinement in a setting for which general character-sum formulas already exist, not a claim to have discovered the entire subset-sum framework. The earlier full-text access gap for [3,4] means there remains a specific priority risk. No independent review has been performed.

## References

1. Zijie Gu, *Subset sums of power values over Galois rings*, arXiv:2610.28837v1, first posted 20 October 2026, https://arxiv.org/html/2610.28837v1; especially Sections 3, 5, 8–9, Appendices A–B.
2. Jiyou Li and Daqing Wan, *On the subset sum problem over finite fields*, Finite Fields Appl. 14 (2008), 911–929, arXiv:0708.2456, https://arxiv.org/abs/0708.2456; exact field expression reproduced in [1], Appendix B.
3. Yuchen Ding and Haiyan Zhou, *Subset sums over Galois rings*, J. Number Theory 205 (2019), 148–169, DOI:10.1016/j.jnt.2019.05.004.
4. Yuchen Ding and Haiyan Zhou, *Subset sums over Galois rings II*, J. Number Theory 252 (2023), 118–136, DOI:10.1016/j.jnt.2023.05.003.
