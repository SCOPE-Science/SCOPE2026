# A two-obstruction Poisson law for generators of finite permutation tense algebras

## Finding

Let \(W\) be a nonempty finite set and \(\sigma\) a permutation of \(W\). On the Boolean algebra \(\mathcal P(W)\), equip the usual Boolean operations with \(\mathbf F(A)=\sigma^{-1}(A)\) and \(\mathbf P(A)=\sigma(A)\), and their Boolean duals \(\mathbf G\) and \(\mathbf H\). This is a tense Boolean algebra. Let \(m_n\) be the number of cycles of \(\sigma\) of length \(n\), let \(q=2^k\), and let
\[
N_n(q)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d},\qquad
(x)_{\underline m}=x(x-1)\cdots(x-m+1),\quad (x)_{\underline0}=1.
\]
Then the number of **ordered** \(k\)-tuples of subsets of \(W\) generating this **entire tense algebra** is exactly
\[
\boxed{G_\sigma(k)=\prod_{n\ge1}n^{m_n}\bigl(N_n(2^k)\bigr)_{\underline{m_n}}},
\]
with factors taken as zero if \(m_n>N_n(2^k)\). Hence its least generator rank (allowing \(k=0\)) is the least \(k\) such that \(m_n\le N_n(2^k)\) for every \(n\).

More sharply, fix an integer \(n\ge1\). Consider a sequence of permutations consisting of \(m=m(q)\) disjoint \(n\)-cycles, with \(q=2^k\to\infty\) and \(m/q^{n/2}\to t\ge0\). Independently choose each of the \(k\) generator subsets uniformly among all subsets. Let \(U\) count cycles with a nonprimitive \(q\)-color word (period smaller than \(n\)); let \(C\) count unordered pairs of distinct cycles whose words are primitive and are equal up to rotation. Then jointly
\[
(U,C)\ \Rightarrow\ 
\bigl(\operatorname{Pois}(\mathbf1_{2\mid n}\,t),
      \operatorname{Pois}(nt^2/2)\bigr),
\]
where the limiting coordinates are independent, and \(\mathbf1_{2\mid n}=1\) for even \(n\) and zero for odd \(n\). Consequently the full-generation probability has the **parity-sensitive birthday limit**
\[
\boxed{\Pr(\text{full generation})\to
\exp\bigl(-\mathbf1_{2\mid n}t-nt^2/2\bigr)}.
\]
For fixed \(n\) and \(m\to\infty\), the deterministic least generator rank is \((\log_2 m)/n+O_n(1)\). In contrast, uniformly random generators succeed with probability tending to one when \(k-(2/n)\log_2m\to+\infty\), and fail with probability tending to one when that difference tends to \(-\infty\). Thus random and existential generator thresholds differ in their leading logarithmic coefficient.

## Assumptions and scope

All worlds and generators are **labelled**: \(\sigma\) is fixed, cycles are distinguishable as subsets of \(W\), and a \(k\)-tuple is ordered. The construction uses the full powerset tense algebra for a finite permutation, not all possible finite tense Boolean algebras. The zero-generator case \(k=0\) is included. The law concerns a fixed common cycle length \(n\) while the number of cycles and the number of truth-value patterns grow. Random generators are independent uniformly chosen subsets, equivalently independent uniform \(q\)-color assignments at all worlds. No randomness is assumed for \(\sigma\).

## Proof

**Tense structure.** The forward and backward operators are Boolean automorphisms inverse to one another. They preserve all finite joins and the zero element, are conjugate in the tense-algebra sense, and their dual box operations satisfy the two adjunction inequalities. In particular the construction belongs to the established class of tense Boolean algebras.

**Itinerary separation.** To a tuple of generators attach its color function \(c:W\to\{0,1\}^k\). Applying all integer powers of the permutation to these generators and taking Boolean combinations produces exactly the Boolean algebra whose atoms are the equivalence classes of
\[
u\sim v\quad\Longleftrightarrow\quad
c(\sigma^j u)=c(\sigma^j v)\ \text{for every integer }j.
\]
Indeed, forward and backward translates give each coordinate predicate of the whole itinerary; finite intersections distinguish any two distinct itinerary vectors, and finiteness makes their fibers single Boolean atoms. Conversely every generated set is constant on these fibers. Thus full generation is equivalent to pairwise distinct itineraries.

On an individual \(n\)-cycle the itineraries are all distinct exactly when its color word has fundamental period \(n\). Two primitive words on separate cycles of equal length yield equal itineraries exactly when they are cyclic rotations of one another. Primitive words of different lengths cannot yield equal infinite itineraries because the fundamental periods differ. These are the **only** two obstructions to full generation.

**Exact count.** Möbius inversion gives \(nN_n(q)=\sum_{d\mid n}\mu(d)q^{n/d}\) primitive words on an \(n\)-cycle. Each primitive necklace has exactly \(n\) distinct rotations. For \(m_n\) individually labelled cycles of length \(n\), choose distinct primitive necklaces in \((N_n(q))_{\underline {m_n}}\) ways and an independent rotation in \(n^{m_n}\) ways. Different lengths are independent. Multiplication gives the displayed enumeration and the generator-rank criterion, including \(n=1\).

**Single-cycle internal defects.** Write \(p_n(q)=1-nN_n(q)/q^n\). For even \(n\), the unique largest proper divisor \(n/2\) contributes \(q^{n/2}\) nonprimitive words; all other proper-divisor contributions are \(O_n(q^{n/3})\). Hence
\[
p_n(q)=q^{-n/2}+O_n(q^{-2n/3})\quad(n\text{ even}).
\]
For odd \(n\ge3\), each proper divisor is at most \(n/3\), so \(p_n(q)=O_n(q^{-2n/3})\). For \(n=1\), \(p_1(q)=0\). Since different cycles are independently colored, \(U\) is binomial with parameters \((m,p_n(q))\). Therefore \(U\Rightarrow\operatorname{Pois}(\mathbf1_{2\mid n}t)\).

**Birthday defects and independence.** Conditional on which cycles are primitive, their necklace classes are independent and uniform on the \(N=N_n(q)\) classes, because every primitive necklace has exactly \(n\) representatives. Since \(N\sim q^n/n\), for \(m/q^{n/2}\to t\), the collision count among the remaining \(m-U\) labels has limiting mean \(\lambda=nt^2/2\). For completeness, the factorial moment of order \(r\) expands over ordered collections of \(r\) *distinct* unordered pairs. The contribution from collections of disjoint pairs is asymptotic to \((m)_{2r}/(2^rN^r)\to\lambda^r\). Any collection having an overlap contains a connected component on \(v\ge3\) vertices and contributes at most order \(m^v/N^{v-1}=O(N^{1-v/2})=o(1)\) relative to bounded disjoint components. Thus every fixed factorial moment converges to that of \(\operatorname{Pois}(\lambda)\), proving the birthday Poisson law. The same argument holds uniformly after deleting any bounded number of cycles. When \(t>0\), \(U\) is tight and \(m\to\infty\), so conditioning on \(U\) and using tightness gives the **independent joint** Poisson limit. If \(t=0\), both defect counts tend to zero in probability by expectation bounds, giving the same conclusion.

The generation event is exactly \(\{U=0,C=0\}\), proving the probability limit. For the outer thresholds, if \(m/q^{n/2}\to0\) then \(\mathbb E(U)+\mathbb E(C)\to0\); if \(m/q^{n/2}\to\infty\), the no-collision probability is at most \(\exp[-m(m-1)/(2N)]\) when \(m\le N\), and is zero when \(m>N\), while nonprimitive cycles only lower success probability. This gives the stated high-probability thresholds. Finally \(N_n(q)\sim q^n/n\) yields the least-rank asymptotic by sandwiching powers of two.

## Verification

A standalone Python 3 script, `checker.py`, derives the predicted counts from Möbius inversion and **independently** constructs the full closure under Boolean and both tense operations for every permutation on one to five worlds, at the specified generator ranks. It evaluates 339 permutation/rank cases and 10,999 ordered color tuples; each predicted count agrees with the direct algebra closure. It also verifies the tense identities in every tested small algebra and evaluates the limiting formula at illustrative finite parameters. Running `python3 checker.py` prints `ALL_CHECKS_OK` if every assertion succeeds. These finite checks do not prove the general enumeration or asymptotic law; those follow from the preceding proofs.

## Relationship to prior work

Figallo, Sarmiento and Pezzini (2026) provide the tense Boolean algebra semantics, syntactic systems and algebraic completeness motivating the finite permutation subclass. Their paper does **not** assert the generator enumeration or the joint Poisson transition. The primitive necklace count \(N_n(q)\) is classical (Möbius–Moreau formula, recorded in OEIS A074650), and the finite coloring criterion is a special form of symmetry-breaking or distinguishing-coloring theory; these ingredients are not claimed as new. Ahmadi, Alinaghipour and Shekarriz (2019/2020) study distinguishing graph colorings and partitions, while Meslem and Sopena (2019/2020) investigate distinguishing parameters for oriented graphs. The present theorem isolates **two simultaneous and independently Poissonian obstructions**, one of which survives only at even cycle lengths, and derives a quantitative separation between existential and random tense-algebra generation. No implication from the inspected primary texts to this full asymptotic statement was identified.

## Limitations

This is a special class of tense Boolean algebras (powersets equipped with a permutation and its inverse). The joint Poisson law assumes a fixed common cycle length as the alphabet size grows. It does not cover growing cycle lengths, arbitrary finite directed frames, or arbitrary finite tense algebras. The exact enumeration inherits known primitive-necklace and distinguishing-coloring principles. The probability limit is an asymptotic theorem, not an exact finite-parameter distribution. A broader existing theorem on distinguishing colorings of disjoint directed cycles or Poisson occupancy could subsume the limiting law; historical priority is not certified. The accompanying computation is illustrative finite verification, not a proof of the infinite statement.

## References

1. M. Figallo, J. Sarmiento, L. Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima's Calculus*, arXiv:2610.01547v1 (first posted 2026-10-01), https://arxiv.org/html/2610.01547v1.
2. B. Ahmadi, F. Alinaghipour, M. H. Shekarriz, *Number of Distinguishing Colorings and Partitions*, arXiv:1910.12102 (2019; 2020 revision), https://arxiv.org/abs/1910.12102.
3. K. Meslem, E. Sopena, *Distinguishing numbers and distinguishing indices of oriented graphs*, arXiv:1910.12738 (2019; 2020 revision), https://arxiv.org/abs/1910.12738.
4. OEIS A074650, *Number of Lyndon words (aperiodic necklaces)*, https://oeis.org/A074650.
