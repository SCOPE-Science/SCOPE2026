# Sharp \(5/2\) approximation at the first positive-cost population for the three-facility Product-Gap rule

## Finding
For four agents at four distinct positions on the real line, the three-facility Product-Gap mechanism has sharp worst-case expected-social-cost approximation factor \(5/2\). The factor is a supremum, not attained at any such profile. Thus its exact first positive-optimum population factor is strictly smaller than the population-uniform factor \(6\) of Jia (2026) and Chan--Lin--Wang (2026).

## Assumptions and scope
Let the four truthful reports be \(t_1<t_2<t_3<t_4\), with adjacent spacings \(x=t_2-t_1>0\), \(y=t_3-t_2>0\), and \(z=t_4-t_3>0\). Three facilities are placed at three distinct reported positions, with each triple \(s_1<s_2<s_3\) selected with probability proportional to \((s_2-s_1)(s_3-s_2)\). Each agent incurs absolute distance to its nearest facility; the social cost is the sum of the four costs. The optimum is allowed to locate facilities at arbitrary real positions and is evaluated without strategic constraints. The ratio is defined only for positive optimum; this holds for the four-distinct-position domain.

## Proof
Every selected triple omits one of the four agents. In order of omitted agent \(1,2,3,4\), its unnormalized weight is
\[
 yz,\quad (x+y)z,\quad x(y+z),\quad xy,
\]
where the notation \(x,y,z\) refers to the positive adjacent gaps above. Their sum equals \(2(xy+xz+yz)\). The corresponding total nearest-facility costs are
\[
 x,\quad \min(x,y),\quad \min(y,z),\quad z.
\]
It follows directly, without approximation, that the expected total cost is
\[
 E=\frac{2xyz+z(x+y)\min(x,y)+x(y+z)\min(y,z)}{2(xy+xz+yz)}.
\]
Any three facilities serving four strictly ordered agents must jointly serve some pair of agents from one facility. The two agents' combined distance to that facility is at least their separation, which is at least \(m=\min(x,y,z)\). Conversely, place facilities at the three reports other than one endpoint of a minimum-gap pair; this achieves total cost \(m\). Hence \(\operatorname{OPT}_3=m\).

Write \(H=xy+xz+yz\) and \(N=2xyz+z(x+y)\min(x,y)+x(y+z)\min(y,z)\). It remains to show \(N<5mH\), because \(E/m=N/(2mH)\). If \(m=x\), set \(h=\min(y,z)\). Then \(h(y+z)\le 2yz\) and
\[
 \frac{N}{x}=3yz+xz+h(y+z)\le5yz+xz<5H.
\]
If \(m=y\), both truncated minima equal \(y\) and
\[
 \frac{N}{y}=4xz+xy+yz<5H.
\]
The case \(m=z\) is obtained by reversing the ordered agents, exchanging \(x\) with \(z\). These inequalities hold strictly for every positive triple, including ties for the minimum.

For the lower bound take \(x=\varepsilon\), \(y=z=1\), where \(\varepsilon>0\) and \(\varepsilon\le1\). The exact ratio is
\[
 \frac{E}{\operatorname{OPT}_3}=\frac{5+\varepsilon}{2(1+2\varepsilon)}\xrightarrow[\varepsilon\downarrow0]{}\frac52.
\]
Thus the supremum is exactly \(5/2\) and is not attained.

## Verification
The accompanying standalone `verify_gap_product.py` uses exact rational arithmetic. It independently enumerates the four possible facility triples and compares the resulting expected-cost ratio with the closed form for each of the \(30^3=27{,}000\) integer adjacent-gap triples in \(\{1,\ldots,30\}^3\), plus \(10{,}000\) additional reproducible integer-gap triples. It checks the strict factor bound on each tested case and verifies the exact limiting formula for four rational gap choices. These finite checks corroborate the algebra but are not substitutes for the universal proof above. Run with `python3 verify_gap_product.py`; the standard Python library is the only dependency.

## Relationship to prior work
Jia, *Product Gap Mechanisms for Multi-Facility Location* (arXiv:2608.19633, publicly available August 20, 2026), defines the mechanism and proves its sharp population-uniform \(2k\) bound, including factor \(6\) for three facilities. Its tightness construction increases the number of agents, so it does not give the exact bound for four agents. Chan, Lin and Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond* (arXiv:2608.22484, August 23, 2026), independently analyzes the equivalent Gap-Product mechanism and proves its population-uniform six-approximation; its separate Inverse-Square rule for almost as many facilities as agents is a different mechanism. This theorem identifies the first positive-cost population's exact constant, not a new strategyproof mechanism or a replacement for the unrestricted guarantee.

## Limitations
The proof is restricted to four agents, three facilities, four distinct real-line reports, nearest-facility absolute-distance cost and the specific Product-Gap sampling weights. It makes no claim for larger populations, duplicate positions, the distinct Inverse-Square mechanism, or alternative metrics. The upper constant is approached through a degenerating gap but is never attained with four distinct reports. Independent validation and exhaustive priority searches across unindexed literature have not been performed.

## References
1. Jianhao Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633 (initial public posting 2026-08-20), https://arxiv.org/abs/2608.19633.
2. Hau Chan, Jianan Lin and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484 (initial public posting 2026-08-23), https://arxiv.org/abs/2608.22484.
