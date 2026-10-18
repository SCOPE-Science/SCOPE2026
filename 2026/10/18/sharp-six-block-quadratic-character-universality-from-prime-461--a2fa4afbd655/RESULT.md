# Sharp six-block quadratic-character universality from prime 461

## Finding
For an odd prime \(p\), put \(\chi_p(0)=0\) and let \(\chi_p(a)\in\{1,-1\}\) for nonzero \(a\in\mathbb F_p\) be the Legendre symbol. For \(\boldsymbol\varepsilon\in\{1,-1\}^6\), define
\[
N_p(\boldsymbol\varepsilon)=\#\{x\in\{1,\ldots,p-6\}:\chi_p(x+j)=\varepsilon_j\text{ for }0\le j<6\}.
\]
Every one of the 64 sign words occurs at least once for **every prime \(p\ge461\)**. The lower cutoff is best possible among primes: at \(p=457\), the word \((1,1,1,1,1,1)\) does not occur. Equivalently, \(457\) is the largest prime at which a nonwrapping six-block pattern is missing.

The cutoff is a statement about *all* 64 patterns simultaneously, not just runs of residues or nonresidues. It is not the first prime at which all 64 occur; the first such prime is \(181\).

## Assumptions and scope
The six entries \(x,x+1,\ldots,x+5\) are taken as ordinary consecutive positive representatives in \(1,\ldots,p-1\); blocks crossing through zero are excluded. The claim covers odd prime moduli and the full 64-word alphabet, without additional congruence assumptions. Squarefree character-sum estimates are used only for primes \(p\ge16384\), where all six shifts are distinct modulo \(p\). A fully specified exact finite enumeration handles all smaller primes.

## Proof
Fix \(\boldsymbol\varepsilon\in\{\pm1\}^{6}\). Extend the ordinary indicator product from the admissible \(x\) to the entire field:
\[
64N_p(\boldsymbol\varepsilon)
=\sum_{x\in\mathbb F_p}\prod_{j=0}^{5}(1+\varepsilon_j\chi_p(x+j))
-\sum_{x\in E}\prod_{j=0}^{5}(1+\varepsilon_j\chi_p(x+j)),
\qquad E=\{0,-1,-2,-3,-4,-5\}.
\]
For \(p>5\), the elements of \(E\) are distinct. At each excluded \(x\) exactly one factor is \(1\), and the five others are in \(\{0,2\}\). Thus the second sum belongs to \([0,192]\).

Expand the first product by subsets \(J\subseteq\{0,\ldots,5\}\). The empty set contributes \(p\); all six singleton character sums vanish. Each of the 15 sums with \(|J|=2\) equals \(-1\), since the corresponding two shifts are distinct. Their total signed contribution is at least \(-15\).

For \(|J|=d\ge3\), the polynomial \(f_J(X)=\prod_{j\in J}(X+j)\) has \(d\) distinct simple roots and is not a square. The Weil bound for a nontrivial quadratic character gives
\[
\left|\sum_{x\in\mathbb F_p}\chi_p(f_J(x))\right|\le(d-1)\sqrt p.
\]
Summing absolute values for \(d=3,4,5,6\) gives
\[
\sum_{d=3}^{6}\binom6d(d-1)=20\cdot2+15\cdot3+6\cdot4+1\cdot5=114.
\]
Therefore, uniformly in the word,
\[
64N_p(\boldsymbol\varepsilon)\ge p-114\sqrt p-207.
\]
If \(p\ge16384=128^2\), writing \(u=\sqrt p\ge128\) gives \(u^2-114u-207\ge128^2-114\cdot128-207=1585>0\) because this quadratic is increasing for \(u\ge128\). Hence every word occurs for all such primes.

It remains to certify the finite range \(p<16384\). The accompanying `verify.py` enumerates **every odd prime** in that range by exact trial division. For each it constructs the complete set of nonzero squares \(\{y^2\bmod p:1\le y<p\}\), scans every admissible start \(1\le x\le p-6\), and records the resulting six-bit word. The two nested finite loops exhaust all words and all starts, so this is a complete finite proof rather than sampling. The program asserts that every prime \(461\le p<16384\) realizes all 64 words; it independently uses Euler's criterion for all primes \(p\le1009\). It also certifies at prime \(457\) that exactly 63 words occur and the unique missing word is \((1,1,1,1,1,1)\). This proves both universality and sharpness.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. The program prints `VERIFY_OK`; it exhaustively processes 1,899 odd primes below \(16384\), including 1,812 primes at least \(461\). The prime \(457\) has exactly one missing word (the six-residue word). The exact arithmetic is limited to integer squares, modular exponentiation and trial division; no floating-point decisions or probabilistic primality testing enter the finite proof. The infinite tail follows from the displayed character-sum inequality independently of computation.

## Relationship to prior work
Davenport's and Weil's classical estimates, reviewed by Wright (arXiv:1111.2236; first publicly available 2011-11-09) and by Conrad in *Quadratic residue patterns modulo a prime*, imply equidistribution of a fixed sign word as \(p\to\infty\). Conrad's Theorem 2.1 gives a general quantitative \(O(\sqrt p)\) estimate, but does not evaluate the **last exceptional prime** for all 64 six-block words. Bennett's 1926 result concerns five consecutive positive quadratic residues, not arbitrary six-sign blocks.

Carella (arXiv:2011.11054) discusses existence of arbitrarily prescribed patterns for sufficiently large primes, without specifying the sharp universal six-block threshold. Buchaev and Tsfasman (arXiv:2607.17418) calculate explicit occurrence formulas for arbitrary patterns of *length four or five*; their Section 2 also recalls the general character-sum/curve expression for any fixed length. Neither a general asymptotic nor that unevaluated expression supplies the cutoff \(461\) without the separate six-block analytic bound and exhaustive finite range established here. All these antecedents are acknowledged; no novelty is claimed for the indicator expansion, quadratic-character sum identities, or the Weil bound themselves.

## Limitations
The statement gives occurrence, not the exact multiplicity of each six-word at every prime. The analytic inequality is deliberately nonoptimal for medium primes, which are resolved by a finite exhaustive certificate. The claim does not cover length seven or higher. Full independent mathematical and literature audits remain unperformed. An unindexed sharp table for the six-block threshold would challenge originality; search and source comparison cannot exclude that possibility categorically.

## References
1. Steve Wright, *Quadratic Residues and Non-residues in Arithmetic Progression*, arXiv:1111.2236, version 1 released 2011-11-09; Journal of Number Theory 133 (2013), 2398–2430. https://arxiv.org/abs/1111.2236
2. Keith Conrad, *Quadratic residue patterns modulo a prime*, Theorem 2.1 and examples. https://kconrad.math.uconn.edu/blurbs/ugradnumthy/QuadraticResiduePatterns.pdf
3. N. A. Carella, *Consecutive Quadratic Residues And Quadratic Nonresidue Modulo p*, arXiv:2011.11054, 2020. https://arxiv.org/abs/2011.11054
4. Abdulkadyr Buchaev and Michael Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418, 2026. https://arxiv.org/abs/2607.17418
5. A. A. Bennett, *Consecutive quadratic residues*, Bulletin of the American Mathematical Society 32 (1926), 283–284, https://doi.org/10.1090/S0002-9904-1926-04211-7
