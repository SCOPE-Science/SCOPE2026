# Exact quantifier-rank profiles for finite one-red linear orders

## Finding
For integers \(a,b\ge 0\), let \(W_{a,b}\) be the finite two-coloured linear order whose colour word is \(B^aRB^b\). Thus there is exactly one red point and every other point is blue. Write \(\equiv_q\) for equivalence in the \(q\)-move Ehrenfeucht--Fraïssé game, equivalently agreement on all first-order sentences of quantifier rank at most \(q\).

At rank \(q=1\), there are exactly two equivalence classes: the one-point word \(R\), and the class of every one-red word containing at least one blue point.

For every \(q\ge 2\), define \(T_q=2^q-1\). Then \(W_{a,b}\equiv_q W_{c,d}\) if and only if exactly one of the following matching shape conditions holds:

1. the red point is first in both words, \(a=c=0\), and \(\min(b,T_q)=\min(d,T_q)\);
2. the red point is last in both words, \(b=d=0\), and \(\min(a,T_q)=\min(c,T_q)\);
3. the red point is interior in both words, \(a,b,c,d>0\), and
\[
\min(a,T_q-1)=\min(c,T_q-1),\qquad
\min(b,T_q-1)=\min(d,T_q-1).
\]

In particular, for \(q\ge2\) there are exactly
\[
1+2T_q+(T_q-1)^2=T_q^2+2=(2^q-1)^2+2
\]
rank-\(q\) classes inside the one-red family. Every such class has a representative of length at most
\[
2(T_q-1)+1=2^{q+1}-3,
\]
and the interior class represented by \(W_{T_q-1,T_q-1}\) shows that this representative-length bound is sharp inside the family.

## Assumptions and scope
The language has a strict linear order and unary colour predicates for \(B\) and \(R\), with the two predicates partitioning the domain. The theorem concerns only finite words in which \(R\) occurs exactly once. Empty words are not part of the family. Quantifier rank is the usual nesting depth of first-order quantifiers.

The primary classification is MSC2020 03C13, model theory of finite structures. The source paper uses the older code 03C64 for this topic; MSC2020 reassigned 03C64 to model theory of ordered structures.

## Proof
Let \(L_n=B^n\) be the monochromatic blue order of length \(n\), allowing \(n=0\). We use two standard facts about Ehrenfeucht--Fraïssé games on coloured linear orders.

First, finite monochromatic linear orders satisfy
\[
L_m\equiv_q L_n
\quad\Longleftrightarrow\quad
\min(m,2^q-1)=\min(n,2^q-1).
\]
Second, for a coloured linear order \(A\) and a point \(x\in A\), its \(q\)-character is the triple consisting of the colour of \(x\), the \(q\)-equivalence class of the segment left of \(x\), and the \(q\)-equivalence class of the segment right of \(x\). Mwesigye and Truss prove that
\[
A\equiv_{q+1} C
\quad\Longleftrightarrow\quad
\rho_q(A)=\rho_q(C),
\]
where \(\rho_q\) is the set of \(q\)-characters realized in the order.

We also use the elementary split lemma. For nonnegative integers \(r,s\) and \(n\ge1\), set
\[
S_{r,s}(n)=\{(\min(i,r),\min(n-1-i,s)):0\le i<n\}.
\]
Then \(S_{r,s}(n)\) depends exactly on \(\min(n,r+s+1)\): two positive integers \(n,n'\) give the same set if and only if
\[
\min(n,r+s+1)=\min(n',r+s+1).
\]
Indeed, before saturation the diagonal \(i+(n-1-i)=n-1\) moves by one with \(n\); once \(n\ge r+s+1\), every further increase occurs only beyond at least one truncation threshold, so the set stabilizes. Conversely, the unsaturated diagonal or the first saturated corner recovers the truncated value.

We now induct on \(q\). At \(q=1\), two coloured orders are equivalent exactly when they realize the same set of colours. Hence \(W_{0,0}\) forms one class and every \(W_{a,b}\) with \(a+b>0\) forms the other.

Assume the stated classification holds at rank \(q\ge1\), and put \(t=2^q-1\). Consider \(\rho_q(W_{a,b})\). Its unique red character is
\[
\bigl(R,[L_a]_q,[L_b]_q\bigr).
\]
The blue characters to the left of the red point are indexed by decompositions \(i+r=a-1\):
\[
\bigl(B,[L_i]_q,[W_{r,b}]_q\bigr),
\qquad 0\le i<a.
\]
The blue characters to the right are symmetrically indexed by decompositions \(j+s=b-1\):
\[
\bigl(B,[W_{a,j}]_q,[L_s]_q\bigr),
\qquad 0\le j<b.
\]

Suppose first that \(b=0\). By the induction hypothesis, the suffix \(W_{r,0}\) remembers \(\min(r,t)\), while the blue prefix \(L_i\) remembers \(\min(i,t)\). The set of left-blue characters therefore contains exactly the split information \(S_{t,t}(a)\). By the split lemma this determines, and is determined by, \(\min(a,2t+1)\). Since \(2t+1=2^{q+1}-1=T_{q+1}\), right-endpoint one-red words have exactly the claimed truncation at rank \(q+1\). The case \(a=0\) is symmetric.

Now suppose \(a,b>0\). For a left-blue point with residual left distance \(r=a-1-i\), the suffix \(W_{r,b}\) is an interior one-red word when \(r>0\), and the induction hypothesis remembers \(\min(r,t-1)\); when \(r=0\), the suffix is the corresponding left-endpoint type, which is separately recognizable and is exactly the unsaturated endpoint of the same split pattern. Thus the left-blue character set contains exactly the split information \(S_{t,t-1}(a)\). By the split lemma it determines, and is determined by, \(\min(a,2t)\). The symmetric right-blue character set determines, and is determined by, \(\min(b,2t)\). Since
\[
2t=2^{q+1}-2=T_{q+1}-1,
\]
this is precisely the claimed interior truncation at rank \(q+1\).

The red character also records whether a side is empty, so endpoint and interior shapes cannot be confused once \(q+1\ge2\). Conversely, if the corresponding truncated data agree, the descriptions above show that the red character and both blue-character sets agree point-for-point as sets of rank-\(q\) types. Therefore \(\rho_q\) is equal, and the character theorem gives \(W_{a,b}\equiv_{q+1}W_{c,d}\). Distinct canonical data give different character sets by the same split lemma, proving the converse.

The class count follows from one all-red singleton class, \(T_q\) positive left-endpoint classes, \(T_q\) positive right-endpoint classes, and \((T_q-1)^2\) interior classes. The representative bound follows by choosing the canonical truncated pair in each class.

## Verification
The accompanying script `verify.py` independently implements the character recursion rather than the closed-form theorem. It constructs the exact rank-\(q\) character set of \(B^aRB^b\) from lower-rank types and compares those recursively computed types with the proposed canonical truncation. It checks ranks \(1\) through \(4\) over rectangles large enough to cross every saturation boundary. A successful run prints four `VERIFY` lines and ends with `VERIFY_OK`.

This computation is finite corroboration only. The all-\(q\) result rests on the induction and split lemma above.

## Relationship to prior work
Mwesigye and Truss study finite coloured linear orders up to Ehrenfeucht--Fraïssé equivalence. Their character theorem supplies the exact one-step recursion used here, and they recall the sharp \(2^q-1\) threshold for monochromatic finite linear orders. They explicitly state that, for general finite coloured linear orders, the classification is not as explicit as in the monochromatic case and provide recursive bounds; their exact general results are for ranks one and two. The present result isolates the natural subfamily with exactly one occurrence of one colour and solves its rank profile in closed form for every rank.

The same paper notes that Bissell--Siders analyzed games on uncoloured linear orders and that those results do not directly apply to coloured linear orders. No searched source or published-finding corpus record was found stating the one-red formula, its class count \((2^q-1)^2+2\), or the sharp representative bound \(2^{q+1}-3\).

## Limitations
The theorem does not classify words with two or more red points, arbitrary two-colour words, infinite coloured orders, quantifier number, formula size, or logics stronger than first-order logic. The web and published-finding corpus searches cannot rule out an unindexed treatment, and the 2009 Leeds thesis cited by Mwesigye and Truss was not inspected; it is the main residual priority risk.

## References
1. F. Mwesigye and J. K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* 28 (2011), 387–397. Published online 7 September 2010. DOI: 10.1007/s11083-010-9178-9.
2. R. Bissell-Siders, “Ehrenfeucht–Fraïssé Games on Linear Orders,” in *Logic, Language, Information and Computation*, LNCS 4576 (2007), 72–82. DOI: 10.1007/978-3-540-73445-1_6.
3. J. G. Rosenstein, *Linear Orderings*, Academic Press, 1982.
