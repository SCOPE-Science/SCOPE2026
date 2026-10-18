# Sharp reversal cutoff and reflection complexity for generalized Thue–Morse words

## Finding

Let \(\ell\ge 3\) be an integer, let \(s_2(j)\) be the number of ones in the binary expansion of \(j\ge0\), and define the infinite word \(\mathbf t_\ell=(s_2(j)\bmod \ell)_{j\ge0}\) on \(\mathbb Z/\ell\mathbb Z\). Write \(\mathcal F_\ell(n)\) for its set of length-\(n\) contiguous factors, \(\rho_\ell(n)=|\mathcal F_\ell(n)|\), and \(r_\ell(n)\) for the number of those factors up to ordinary word reversal (without complementing letters).

**Theorem.** For every integer \(\ell\ge3\):

1. No length-\(4\) factor of \(\mathbf t_\ell\) has its ordinary reversal in the language: \(\mathcal F_\ell(4)\cap \{w^R:w\in\mathcal F_\ell(4)\}=\varnothing\). Consequently, the same holds at every length \(n\ge4\), and \(\mathbf t_\ell\) has no palindromes of length at least \(4\).
2. Every reflected factor of length \(3\) is a palindrome. Thus \(r_\ell(n)=\rho_\ell(n)\) for every \(n\ge3\). In particular this proves the previously proposed generalized Thue–Morse reflection-complexity identity for every \(\ell\ge4\), including the modulus-four case not specified by that conjecture.
3. All \(\ell^2\) ordered length-\(2\) factors occur, and all \(2\ell^2-\ell\) length-\(3\) factors whose consecutive-difference vector contains \(1\) occur. Consequently, the *complete short-length exceptions* are \(r_\ell(0)=1\), \(r_\ell(1)=\ell\), \(r_\ell(2)=\ell(\ell+1)/2\), and \(r_\ell(3)=2\ell^2-\ell\). There are exactly \(2\ell\) palindromic length-\(3\) factors, and none of length at least four.

In particular, the first possible length at which **no** factor has an occurring reversal is exactly \(4\); length \(3\) still has palindromic factors.

## Assumptions and scope

The alphabet is the additive cyclic group \(\mathbb Z/\ell\mathbb Z\) with \(\ell\ge3\); all displayed differences are interpreted modulo \(\ell\). The sequence is indexed from \(0\). A factor is a contiguous finite substring; its reversal reverses positions but does not negate letters or apply a dihedral antimorphism. Equality \(r_\ell(n)=\rho_\ell(n)\) compares the *same factors* under the relation \(u\sim v\) iff \(u=v\) or \(u=v^R\), irrespective of whether \(v\) is otherwise a factor. The empty factor is included at length zero.

## Proof

For every \(m\ge0\), binary digit sums give
\[
\mathbf t_\ell(2m)=\mathbf t_\ell(m),\qquad
\mathbf t_\ell(2m+1)=\mathbf t_\ell(m)+1\pmod\ell.
\]
Set \(a=\mathbf t_\ell(m)\), \(b=\mathbf t_\ell(m+1)\), and \(c=\mathbf t_\ell(m+2)\). A length-four factor starting at even position \(2m\) is
\[
(a,a+1,b,b+1).
\]
Its three successive differences are of form \((1,d,1)\), with arbitrary \(d\in\mathbb Z/\ell\mathbb Z\). A length-four factor starting at odd position \(2m+1\) is
\[
(a+1,b,b+1,c).
\]
If \(m\) is even, \(b=a+1\), so the differences have form \((0,1,d)\). If \(m\) is odd, \(c=b+1\), so they have form \((d,1,0)\). Thus every occurring difference triple belongs to
\[
E=\{(1,d,1):d\in\mathbb Z/\ell\mathbb Z\},\quad
L=\{(0,1,d):d\in\mathbb Z/\ell\mathbb Z\},\quad
R=\{(d,1,0):d\in\mathbb Z/\ell\mathbb Z\}.
\]
Reversal transforms the difference triple \((u,v,w)\) into \((-w,-v,-u)\). Since \(\ell\ge3\), \(-1\ne1\) and \(-1\ne0\) modulo \(\ell\). The reversal of an element of \(E\) has first and last entries \(-1\), and so lies in none of \(E,L,R\). The reversal of an element of \(L\) or \(R\) has middle entry \(-1\), which excludes \(L,R\), and one outer entry \(0\), which excludes \(E\). Hence a length-four factor cannot occur together with its reversal. If a length-\(n\) factor for \(n>4\) occurred together with its reversal, its first four letters and their reversal would both occur as length-four factors; this is impossible. This establishes assertion 1, including the palindrome statement.

For any occurring length-three factor, its two successive differences contain \(1\): starts at even positions have first difference \(1\), and starts at odd positions have second difference \(1\). If both \(w\) and \(w^R\) occur, the original difference pair must contain both \(1\) and \(-1\). These are distinct modulo \(\ell\), so the pair is precisely \((1,-1)\) or \((-1,1)\). In either case the first and third symbols of \(w\) coincide; \(w\) is a palindrome. Therefore no two *distinct* length-three factors are reflectively equivalent, and the same is true at greater lengths by assertion 1. This proves assertion 2.

For assertion 3 we first show that every ordered pair \((A,B)\in(\mathbb Z/\ell\mathbb Z)^2\) occurs. Choose integers \(k,r\ge0\) satisfying \(k\equiv A-B\pmod\ell\) and \(r\equiv B-1\pmod\ell\). Put \(q=2^r-1\) and \(m=2^{k+1}q+2^k-1\). Since these are disjoint binary blocks,
\[
s_2(m)=r+k,\qquad s_2(m+1)=r+1.
\]
The length-two factor starting at \(2m+1\) is
\[
\big(\mathbf t_\ell(2m+1),\mathbf t_\ell(2m+2)\big)
=\big(r+k+1,r+1\big)=(A,B)\pmod\ell.
\]
Thus \(\mathcal F_\ell(2)\) is the entire set of ordered pairs. The even-start length-three factors \((a,a+1,b)\) exhaust all triples whose first difference is \(1\); the odd-start length-three factors \((a+1,b,b+1)\) exhaust all triples whose second difference is \(1\). Each family has \(\ell^2\) members and their intersection (both differences \(1\)) has \(\ell\), giving \(\rho_\ell(3)=2\ell^2-\ell\). Of these triples the palindromes are exactly the \(\ell\) with differences \((1,-1)\) and the \(\ell\) with differences \((-1,1)\); they are distinct because \(\ell\ge3\). At length two, reversing identifies \((A,B)\) with \((B,A)\) and gives \(\ell(\ell+1)/2\) classes. Length-one letters all occur by the ordered-pair argument, and the empty factor contributes one class. The theorem follows. \(\square\)

## Verification

The independent executable `verify.py` checks both the global three-difference-family obstruction for moduli \(3\) through \(63\) and the constructive realization of all ordered pairs for moduli \(3\) through \(34\), using direct bit-count calculations at the constructed positions. It separately enumerates factors and reversal classes in explicitly finite prefixes for moduli \(3\) through \(8\), lengths through \(12\). The proof above, not these bounded tests, establishes the statements for all integer moduli and all factor lengths. Run from this package with `python3 verify.py`.

## Relationship to prior work

Allouche, Campbell, Li, Shallit, and Stipulanti (2024, arXiv:2406.09302) introduced reflection complexity and explicitly asked for its extension to generalized Thue–Morse words. Their further-directions discussion reports equality for modulus three and an apparent analogous identity for moduli greater than four, without proving those further moduli. The present theorem proves the predicted reflection identity for all moduli at least four and gives a stronger, sharp length-four reversal obstruction plus exact short-length counts.

Starosta (2011 preprint; 2012 article) computed ordinary factor complexity and established symmetry under *dihedral antimorphisms* of generalized Thue–Morse words. Those antimorphisms reflect and also exchange alphabet letters; for \(\ell\ge3\), this is not the same as plain reversal of an unmodified word. Their symmetry and factor-complexity statements therefore do not imply the asserted cutoff or reflection identity. Fleischer and Shallit (2019) classified languages of words avoiding reversed factors but did not establish this precise infinite-family identification. Later work of Dvořáková and Pelantová (2025 preprint) develops general reflection-complexity theory, but the inspected analysis concerns different classes of sequences and does not imply the present specific cutoff.

## Limitations

The result concerns binary digit sums reduced modulo \(\ell\ge3\), not digital sums in other bases, nor the ordinary binary Thue–Morse word (\(\ell=2\)); the crucial inequality \(1\ne-1\pmod\ell\) fails when \(\ell=2\). The formula for \(r_\ell(n)\) at arbitrary \(n\ge4\) is an equality with the **previously known ordinary factor complexity**, not a newly derived independent closed form for that function. The mathematical novelty assessment uses available published sources and research records; undetected equivalent earlier work remains a possibility. No external independent validation has been performed.

## References

1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first posted 2024-06-13), specifically the further-directions question on generalized Thue–Morse words and the reflection-complexity definitions. https://arxiv.org/abs/2406.09302
2. Š. Starosta, *Generalized Thue–Morse words and palindromic richness*, arXiv:1104.2476 (2011), Kybernetika 48 (2012), 361–370. https://arxiv.org/abs/1104.2476
3. L. Fleischer and J. Shallit, *Words Avoiding Reversed Factors, Revisited*, arXiv:1911.11704 (2019). https://arxiv.org/abs/1911.11704
4. L. Dvořáková and E. Pelantová, *Reflection on the Reflection Complexity*, arXiv:2511.12358 (2025). https://arxiv.org/abs/2511.12358
