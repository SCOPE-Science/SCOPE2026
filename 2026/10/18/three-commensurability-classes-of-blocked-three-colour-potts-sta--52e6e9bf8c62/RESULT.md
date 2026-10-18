# Three commensurability classes of blocked three-colour Potts states on complete tripartite graphs

## Finding
Let \(G_n=K_{n,n,n}\), with three labelled parts of size \(n\ge1\), and let each vertex carry one of three labelled Potts colours. Take the antiferromagnetic energy \(H(\sigma)\) to be the number of edges whose endpoint colours agree. A configuration is **blocked** when recolouring any one vertex to either of the other two colours does not *strictly decrease* \(H\); zero-energy-change recolourings are allowed.

Write \(B_n\) for the number of blocked labelled configurations and \(Z_n(y)=\sum_{\sigma\,\mathrm{blocked}}y^{H(\sigma)}\). For every \(n\) not divisible by three,
\[
Z_n(y)=6+\mathbf 1_{2\mid n}\left[9\binom{n}{n/2}^{2}y^{n^2/2}+6\binom{n}{n/2}^{3}y^{3n^2/4}\right].
\]
(The binomial coefficient and the second term occur only when \(n\) is even.) In particular, \(B_n=6\) whenever \(\gcd(n,6)=1\); then the only blocked states are the six proper three-colourings, each monochromatic on a different part.

For every \(n\) divisible by three, independently of parity,
\[
\left[\frac{n!}{((n/3)!)^3}\right]^3\le B_n\le 3^{3n}.
\]
Consequently the normalized blocked-state entropy \(s_n=(3n)^{-1}\log B_n\) has exactly the following three limits along residue classes:
\[
\lim_{\substack{n\to\infty\\n\equiv1,5\pmod6}}s_n=0,\qquad
\lim_{\substack{n\to\infty\\n\equiv2,4\pmod6}}s_n=\log2,\qquad
\lim_{\substack{n\to\infty\\n\equiv0,3\pmod6}}s_n=\log3.
\]
Thus the unrestricted blocked-state entropy density does not exist. These are entropy limits for kinetically blocked configurations, **not** equilibrium phase-transition claims.

## Assumptions and scope
The graph has no edges within parts and every edge between different parts. All three parts have the same positive integer size \(n\), all three colours are globally available at every vertex, and every edge has equal positive antiferromagnetic coupling, normalized to one. The dynamics allows single-vertex recolouring only when it strictly decreases energy. The claim counts distinct labelled spin configurations; vertices within a part are not identified under permutations. The exact polynomial is claimed only for \(3\nmid n\), while the entropy limit on \(3\mid n\) uses the stated rigorous upper and lower bounds.

## Proof
**1. Local blocking condition.** For part \(i\in\{1,2,3\}\) and colour \(c\in\{1,2,3\}\), let \(x_{ic}\) be the number of vertices of colour \(c\) in part \(i\); thus \(\sum_c x_{ic}=n\). Define the number of exterior vertices of colour \(c\) by \(m_{ic}=\sum_{j\ne i}x_{jc}\). A recolouring \(c\to d\) at a vertex of part \(i\) changes energy by \(m_{id}-m_{ic}\). Hence blocking is equivalent to: every colour present in part \(i\) attains \(\min_d m_{id}\).

All three colours must be used. Indeed, if one colour were absent globally, its exterior count would be zero everywhere. Every used colour would then have to occur in only one part; two or fewer used colours cannot support three nonempty parts.

**2. Three-supported part.** If one part uses all three colours, its three exterior counts are equal. Their sum is \(2n\); thus each equals \(2n/3\), an integer. Therefore \(3\mid n\). Consequently for \(3\nmid n\), every part uses at most two colours.

**3. A colour confined to one part.** Suppose a colour occurs only in part \(i\). Its exterior count in \(i\) is zero, so stability forces *every* colour used in part \(i\) to occur nowhere else. If this part used two exclusive colours, the remaining two parts could use only the third colour, and either remaining part could improve by recolouring to an exclusive colour having fewer than \(n\) neighbours: impossible. Hence \(i\) is monochromatic in one exclusive colour. The other two parts use the other two colours. If both are monochromatic, they must have different colours, yielding the six proper states. Otherwise both parts must use both remaining colours: equal exterior counts force each to contain \(n/2\) vertices of each, so \(n\) is even. These states have energy \(n^2/2\). There are three choices for the exceptional part, three for its colour, and \(\binom n{n/2}^2\) labelled choices: altogether \(9\binom n{n/2}^2\). (The proper states are counted only once.)

**4. No exclusive colour.** Every one of the three colours then occurs in at least two parts, hence the support matrix has at least six positive cells. By Step 2 it has at most six. It therefore has exactly six, with every part containing two colours and every colour appearing in two parts. The absent colours form a bijection between the three parts and the three colours, giving six support patterns. Write \(a_i\) for the common minimum of the exterior colour counts in part \(i\). If colour \(c\) is shared by parts \(i,j\) but absent from the third part, the counts satisfy \(x_{ic}=a_j\) and \(x_{jc}=a_i\). Each part shares its two colours with the other two parts, so \(n=a_j+a_k\) for every permutation of \(i,j,k\). Therefore all \(a_i=n/2\), requiring \(n\) even. Each present colour occupies exactly \(n/2\) sites in its part. The absent colour has exterior count \(n\), so these configurations are indeed blocked. There are \(6\binom n{n/2}^3\) of them, each with three monochromatic cross-part edge blocks of size \((n/2)^2\), hence energy \(3n^2/4\).

Steps 1–4 exhaust all configurations when \(3\nmid n\), establishing the full energy polynomial.

**5. Entropy subsequences.** If \(3\mid n\), colouring exactly \(n/3\) sites of each part in each colour makes every exterior colour count equal to \(2n/3\), and is blocked. There are exactly \(\big[n!/((n/3)!)^3\big]^3\) such configurations. All \(3^{3n}\) colourings give an upper bound. By Stirling's formula, the logarithms of these bounds divided by \(3n\) both tend to \(\log3\). If \(n\equiv2,4\pmod6\), the exact expression is \(6+9\binom n{n/2}^2+6\binom n{n/2}^3\); Stirling gives its normalized logarithm tending to \(\log2\). If \(n\equiv1,5\pmod6\), the exact count is six, yielding zero. All three residue families are infinite, completing the claim.

## Verification
The standalone `verify.py` uses no third-party packages. It independently recomputes energy differences from the original labelled spin configurations for \(n=1,2,3\), and compares those results with the occupation-matrix blocking criterion. It exhaustively enumerates all occupation matrices for \(1\le n\le12\), weights each by exact multinomial coefficients, checks the complete energy polynomial for every \(3\nmid n\) in that range, and checks the lower/upper bounds for \(3\mid n\). The script completed successfully with 20,470 assertions/check counters. Exhaustive finite checks are supplementary: the proof above establishes the theorem for all integers in its stated scope.

## Relationship to prior work
Kotecký, Sokal and Swart study the three-state antiferromagnetic Potts model and entropy-driven ordering on infinite planar quadrangulations, with a 2012 public preprint. Their zero-temperature ground states are proper colourings; they do not derive the blocked-state enumeration for the dense complete tripartite graph. Kun, Powers and Reyzin (2013) define the same one-vertex best-response stability notion as *stable graph colourings* and prove general existence, potential-game, and price-of-anarchy results. Those results are foundational but do not supply the present all-size polynomial or three-residue entropy law. The balanced bipartite case has a different support structure: in the tripartite case every proper three-colouring is forced to be monochromatic on each part, allowing complete collapse to six blocked states for infinitely many sizes. Claims of novelty concern the explicit tripartite classification and entropy trichotomy, not the underlying best-response definition or general Potts model.

## Limitations
No exact full blocked-state polynomial is claimed when \(3\mid n\); only the displayed bounds and entropy limit are established in that regime. Energy-neutral recolourings are forbidden dynamically but allowed in the definition of blocking; allowing such moves changes the absorbing-state interpretation. Neither dynamical probabilities of entering particular blocked configurations, nor mixing times, finite-temperature transitions, or unequal part sizes are addressed. The literature comparison is based on the sources inspected; independent literature validation has not been performed.

## References
1. R. Kotecký, A. D. Sokal and J. M. Swart, *Entropy-driven phase transition in low-temperature antiferromagnetic Potts models*, arXiv:1205.4472 (first public version 21 May 2012), https://arxiv.org/abs/1205.4472.
2. J. Kun, B. Powers and L. Reyzin, *Anti-Coordination Games and Stable Graph Colorings*, arXiv:1308.3258 (first public version 14 August 2013), https://arxiv.org/abs/1308.3258.
