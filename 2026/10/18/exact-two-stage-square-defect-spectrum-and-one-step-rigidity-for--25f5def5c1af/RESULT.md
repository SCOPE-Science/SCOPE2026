# Exact two-stage square-defect spectrum and one-step rigidity for reciprocal-sum sequences

## Finding

Let \(h\ge1\) and \(x_0\ge1\) be integers and set
\[
x_{n+1}=\frac{h^2}{x_0+\cdots+x_n}\quad(n\ge0),\qquad
x_n=\frac{a_n}{b_n}\text{ in lowest positive terms},\qquad
Q_n=\frac{2a_n}{h}+b_n\quad(n\ge2).
\]
A defect at index \(n\) means that \(Q_n\) is not the square of an integer. For a prime power \(p^a\Vert h\), set \(c_{p,2}\) and \(c_{p,3}\) by the following complete local table:

| Condition on \(p\) | \(c_{p,2}\) | \(c_{p,3}\) |
|:--|--:|--:|
| \(p=2\) | 1 | 0 |
| \(p\equiv3\pmod4\) | 0 | 0 |
| \(p=5\) | 2 | 2 |
| \(p\equiv13,17\pmod{20}\) | 2 | 0 |
| \(p\equiv1,9\pmod{20}\) | 2 | 4 |

Write \(\alpha_p=c_{p,2}/p^{a+1}\), \(\beta_p=c_{p,3}/p^{a+1}\), and let \(F_2,F_3\) denote the two defects. All products below range over the distinct primes dividing \(h\); empty products equal \(1\). **The exact natural densities of starting values \(x_0\)** are
\[
\begin{aligned}
\Pr(F_2)&=1-\prod_{p\mid h}(1-\alpha_p),\\
\Pr(F_3)&=1-\prod_{p\mid h}(1-\beta_p),\\
\Pr(F_2\cap F_3)&=1-\prod_{p\mid h}(1-\alpha_p)-\prod_{p\mid h}(1-\beta_p)
                  +\prod_{p\mid h}(1-\alpha_p-\beta_p),\\
\Pr(\neg F_2\cap\neg F_3)&=\prod_{p\mid h}(1-\alpha_p-\beta_p).
\end{aligned}
\]
Indeed, these are exact proportions over every complete period \(L=h\,\mathrm{rad}(h)\) of positive starting values, not just asymptotic limits.

**Sharp one-step rigidity.** For every positive starting value \(x_0\), all defects occur at index \(2\), if any, **if and only if**
\[
5\nmid h\quad\text{and}\quad p\nmid h\ \text{for every prime }p\equiv1,9\pmod{20}.
\]
Equivalently, every odd prime divisor of \(h\) is either \(3\pmod4\) or \(13,17\pmod{20}\). Under this condition the total number of defects over all \(n\ge2\) is a Bernoulli random variable (with respect to natural density of \(x_0\)): it is \(1\) with probability \(1-\prod_{p\mid h}(1-\alpha_p)\) and \(0\) otherwise.

For example, \(h=13\) has a defect only potentially at index \(2\), with exact probability \(2/169\). For \(h=26\) the corresponding probability is \(175/676\), and there are no later defects for any starting value. Conversely, \(5\mid h\) or some \(p\mid h\) with \(p\equiv1,9\pmod{20}\) guarantees a starting value having a defect at index \(3\).

## Assumptions and scope

The recurrence is over positive rational numbers. The starting integers range over \(x_0\in\mathbb N\); the parameter \(h\) ranges over all positive integers. All probabilities refer to natural density in that starting integer, with \(h\) fixed. No probability measure on the positive rationals or on the parameter is assumed. A perfect square means the square of an integer, not merely of a rational. The local quantities depend on \(a=\nu_p(h)\) through their denominators, and not only on the residue of the prime. The asserted Bernoulli law counts all indices \(n\ge2\), not just the first two.

## Proof

**1. Primitive recurrence and defect criterion.** Put \(S_n=x_0+\cdots+x_n\) and write \(S_n/h=u_n/v_n\) in coprime positive integers. Initially
\[
(u_0,v_0)=\left(\frac{x_0}{g},\frac{h}{g}\right),\qquad g=\gcd(x_0,h),
\]
and, without cancellation,
\[
(u_{n+1},v_{n+1})=(u_n^2+v_n^2,\;u_nv_n).
\]
The absence of cancellation follows from \(\gcd(u_n,v_n)=1\). Let \(d_n=\gcd(h,u_n)\). Since \(x_{n+1}=hv_n/u_n\), for \(n\ge1\) reduction gives
\[
Q_{n+1}=\frac{(u_{n-1}+v_{n-1})^2}{d_n}.
\]
If an odd \(p\mid d_n\), then \(p\nmid u_{n-1}+v_{n-1}\): otherwise \(u_{n-1}^2+v_{n-1}^2\equiv-2u_{n-1}v_{n-1}\pmod p\), with both factors units, contradicting \(p\mid u_n\). Thus \(Q_{n+1}\) has negative \(p\)-adic valuation. If \(2\mid d_n\), then \(u_{n-1},v_{n-1}\) are odd, \(\nu_2(u_n)=1\), and \(Q_{n+1}\) has odd \(2\)-adic valuation. Conversely \(d_n=1\) makes \(Q_{n+1}\) an integer square. Therefore
\[
F_j\quad\Longleftrightarrow\quad \gcd(h,u_{j-1})>1\qquad(j\ge2).
\]
If \(p\mid u_j\), then \(p\nmid v_j\), while \(u_{j+1}\equiv v_j^2\not\equiv0\) and \(v_{j+1}\equiv0\pmod p\); induction shows \(p\) cannot divide any later \(u_m\). Hence one fixed prime cannot independently cause both \(F_2\) and \(F_3\), or more than one defect index.

**2. Exact local starting classes.** Fix \(p^a\Vert h\). If \(\nu_p(x_0)\ne a\), the primitive initial pair has exactly one of \(u_0,v_0\) divisible by \(p\), so \(u_1\equiv u_0^2+v_0^2\not\equiv0\pmod p\), and no later numerator becomes divisible by \(p\). If \(\nu_p(x_0)=a\), write \(x_0=p^a y\), \(h=p^a H\), where \(p\nmid yH\). Then \(u_0/v_0\equiv yH^{-1}\pmod p\). Each nonzero \(z\in\mathbb F_p\) corresponds bijectively to one residue class of \(x_0\pmod{p^{a+1}}\), namely \(x_0\equiv p^a Hz\pmod{p^{a+1}}\).

For the projective map \(T(z)=z+z^{-1}\), extended by \(T(0)=T(\infty)=\infty\), these are exactly the finite nonzero initial classes. A defect \(F_j\) arises locally precisely when \(T^{j-1}(z)=0\). The depth-one preimages solve \(z^2+1=0\). There is one such \(z\) for \(p=2\), none for odd \(p\equiv3\pmod4\), and two for odd \(p\equiv1\pmod4\). Their numbers are the \(c_{p,2}\) column.

**3. Depth-two roots and the modulus \(20\) dichotomy.** Over \(\mathbb F_2\), \(T(1)=0\) but no finite nonzero argument maps to \(1\); the depth-two set is empty. Over odd fields with \(p\equiv3\pmod4\) it is also empty. If \(p\equiv1\pmod4\), choose \(i\) with \(i^2=-1\). A depth-two starting class satisfies \(T(z)=i\) or \(T(z)=-i\), that is,
\[
z^2-iz+1=0\quad\text{or}\quad z^2+iz+1=0.
\]
Both discriminants are \(-5\). For \(p=5\) each quadratic has a repeated root, yielding two distinct depth-two classes altogether. For \(p\ne5\), each quadratic has two distinct roots if \(-5\) is a quadratic residue and none if it is a nonresidue. The two root sets are disjoint: a common nonzero root would satisfy \(2iz=0\). Quadratic reciprocity for \(p\equiv1\pmod4\) gives \(\left(\frac{-5}{p}\right)=\left(\frac{p}{5}\right)\); it equals \(1\) at \(p\equiv1,9\pmod{20}\) and \(-1\) at \(p\equiv13,17\pmod{20}\). This proves the complete \(c_{p,3}\) column. No depth-two root lies at depth one, since after a numerator becomes zero the projective orbit is at \(\infty\) forever.

**4. Chinese-remainder independence.** The local defect sets depend only on \(x_0\pmod{p^{a+1}}\), with exactly \(c_{p,2}\) and \(c_{p,3}\) classes, and these two sets are disjoint. The pairwise coprime moduli \(p^{a+1}\), whose product is \(L=h\mathrm{rad}(h)\), give independent residue choices by the Chinese remainder theorem. Multiplying the probabilities of absence gives the first, second, and fourth displayed formulas. Inclusion-exclusion gives the intersection formula. Every finite union of residue classes modulo \(L\) has natural density equal to its fraction of classes, proving all assertions about the first two indices.

**5. Sharp rigidity for every later index.** If no prime dividing \(h\) has a depth-two preimage of zero, it has no depth-\(r\) preimage for any \(r\ge2\): a longer preimage would map to a depth-two preimage after enough iterations. Thus no \(u_j\) is divisible by a prime of \(h\) for \(j\ge2\), proving that only \(F_2\) can occur for all \(x_0\). Conversely if such a prime \(p\) has a depth-two starting class \(z\), choose a positive integer \(e\equiv z\pmod p\) and set \(x_0=he\). The initial primitive pair is \((e,1)\), forcing \(p\mid u_2\) and hence \(F_3\). The local table characterizes precisely those primes with nonempty depth-two preimages, proving necessity, sufficiency, and the complete Bernoulli distribution.

## Verification

The standalone Python-standard-library script `verify.py` checks exact residue classes over one full modulus \(L\) for many values of \(h\); independently evaluates the first two defect indicators using exact rational recurrence fractions; examines later numerators for primes in the rigid family; and constructs explicit third-index failure witnesses for forbidden primes. Its tested outputs are 155065 residue classes, 2280 exact rational comparisons, 13101 later-indicator checks, and eight witnesses, terminating with `VERIFY_OK`. Run `python3 verify.py` with Python 3. Finite tests do not prove the infinite theorem; Steps 1–5 do.

## Relationship to prior work

Matijasevick–Rodríguez–Salazar (2026), Proposition 2.3 and 4.1, establish the exact square-defect criterion, at-most-one-failure-per-prime law, and pose explicitly in Section 7, Question (1), the problem of determining proportions of starting values with prescribed numbers of failures. Those ingredients and the recurrence are credited, not presented as new. The result above computes the **complete joint distribution at the first two indices for every \(h\)** and solves the full all-index failure-count problem on the precisely classified infinite rigid family. It improves the known uniform later-defect cutoff for primes \(p\equiv13,17\pmod{20}\) to index 2. Ugolini (2013/2014) develops the preimage-graph theory of related maps \(z\mapsto k(z+z^{-1})\); solving inverse quadratics and using their discriminants are standard. The specific link between depth-two arithmetic, exact starting-density formulas, and sharp reciprocal-sum rigidity is the contribution assessed here, not the discriminant calculation alone.

## Limitations

Outside the rigid family, a defect at index \(3\) can occur, but this theorem does not determine the complete count distribution over all later indices. It does not claim novelty for the elementary local inverse calculation, the square criterion, or the general bounded-failure theorem. An unlocated companion manuscript by Matijasevick on zeros of iterates, cited in the motivating preprint, could contain closely related depth-specific estimates; this remains a literature-overlap risk. The published global dynamics literature also merits independent further comparison. No independent mathematical audit has been performed.

## References

1. M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (first publicly posted 2026-09-30), Sections 2, 4, and 7. https://arxiv.org/abs/2610.00765
2. S. Ugolini, *On the iterations of certain maps \(x\mapsto k(x+x^{-1})\) over finite fields of odd characteristic*, arXiv:1304.3283v2, *Journal of Number Theory* 142 (2014), 274–297. https://arxiv.org/abs/1304.3283
3. R. Jones and M. Manes, *Galois theory of quadratic rational functions*, *Commentarii Mathematici Helvetici* 89 (2014), 173–213, arXiv:1101.4339. https://arxiv.org/abs/1101.4339
