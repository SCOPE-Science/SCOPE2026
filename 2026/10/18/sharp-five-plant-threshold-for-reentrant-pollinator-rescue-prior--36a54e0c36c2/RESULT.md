# Sharp five-plant threshold for reentrant pollinator-rescue priorities

## Finding

**Theorem (sharp minimum for reentrant conservation ranking).** In the binary plant–pollinator protection model defined below, with any positive finite number of pollinator species and with at most four plant species, no pollinator can be the unique optimal single-species protection target at two failure probabilities while being strictly suboptimal at a failure probability between them. Five plant species suffice: an explicit five-plant, seven-pollinator network has a single target that is uniquely optimal at low and high background failure probabilities, but a different target is uniquely optimal in a nonempty interval between them. For that network the optimum changes exactly twice as the common failure probability increases through \((0,1)\).

The theorem is a sharp cutoff in the **number of plants**, not a claim of the smallest pollinator count, and applies to an expected-richness objective rather than a whole-network probability of survival.

## Assumptions and scope

Let \(\mathcal P\) and \(\mathcal R\) be finite disjoint sets of plant and pollinator species, respectively. Let \(E\subseteq\mathcal P\times\mathcal R\) be a simple bipartite interaction relation. Every plant has at least one pollinator. Write \(N(i)\) for the pollinators adjacent to plant \(i\), and \(d_i=|N(i)|\). Without intervention, each pollinator independently disappears with the same probability \(q\in(0,1)\). A plant persists exactly when at least one of its original pollinators persists; plant species have equal unit weight, and there are no secondary effects or interaction rewiring. An intervention guarantees that a single selected pollinator \(j\) survives, without changing other pollinators' independent failure probabilities. The objective is the expected number of persistent plants, and each intervention has identical cost.

Let \(\mathbb E_0(q)\) be the expected number of plants without intervention and \(\mathbb E_j(q)\) the expectation when pollinator \(j\) is protected. The absolute gain and its ranking-equivalent normalization are
\[
G_j(q)=\mathbb E_j(q)-\mathbb E_0(q)=\sum_{i:\,j\in N(i)}q^{d_i},
\qquad H_j(q)=G_j(q)/q=\sum_{i:\,j\in N(i)}q^{d_i-1}.
\]
Because \(q>0\), maximizing \(G_j\) is exactly equivalent to maximizing \(H_j\). A target is **uniquely optimal** if its gain is strictly larger than every other target's gain. A target **reenters** if there exist \(0<q_1<q_2<q_3<1\) at which it is uniquely optimal at \(q_1,q_3\), but is not an optimizer at \(q_2\).

## Proof

**Gain identity.** Plant \(i\) disappears in the untreated system exactly when all \(d_i\) neighboring pollinators fail, an event of probability \(q^{d_i}\). If \(i\) is adjacent to the protected pollinator, that plant cannot disappear after protection; otherwise its disappearance probability does not change. Linearity of expectation gives the displayed formulas for \(G_j\) and \(H_j\), without requiring independence of the different plant-survival indicators.

**No reentry with four or fewer plants.** For any two pollinators \(a,b\), shared neighboring plants cancel, so
\[
H_a(q)-H_b(q)
=\sum_{i\in N(a)\setminus N(b)}q^{d_i-1}
-\sum_{i\in N(b)\setminus N(a)}q^{d_i-1}.
\]
This is a signed sum of at most four monomials, with a plus or minus sign attached to each plant. If all signs agree, the difference has constant sign. If one sign occurs only once, either some monomial with the opposite sign has exponent at most the singleton's exponent (so it cancels or dominates that singleton for every \(0<q<1\), leaving the other terms of constant sign), or every opposite-sign monomial has larger exponent. In the latter case, dividing by the singleton monomial reduces the question to whether a strictly increasing sum of positive integer powers of \(q\) crosses the value one: this can occur at most once. Equal exponents are covered by the first case.

It remains to consider two positive and two negative monomials. Combine equal powers and discard zero coefficients, then order the remaining powers increasingly. If the ordered signs change at most twice, Descartes' rule of signs yields at most two positive real zeros, counted with multiplicity. Yet \(q=1\) is already a positive zero because two plus and two minus monomials have equal total count. There can therefore be at most one zero in \((0,1)\). If the signs change three times, all four distinct exponents \(a<b<c<d\) have alternating unit coefficients, and the difference or its negative is \(q^a-q^b+q^c-q^d\). This is strictly positive for \(0<q<1\) since both \(q^a-q^b\) and \(q^c-q^d\) are strictly positive. Thus for any two targets the difference cannot change from strictly positive to strictly negative and back on \((0,1)\).

Suppose target \(a\) were uniquely best at \(q_1\) and \(q_3\), but not optimal at an intermediate \(q_2\). There would be a target \(b\) with \(H_b(q_2)>H_a(q_2)\). Then \(H_a-H_b\) would be strictly positive at \(q_1,q_3\) and strictly negative at \(q_2\), giving at least two distinct interior zeros, contrary to the pairwise conclusion. Therefore no reentry is possible for at most four plants.

**Attaining reentry with five plants.** Take seven pollinators \(A,B,F_1,F_2,F_3,F_4,F_5\). The five plant neighborhoods are exactly
\[
\begin{aligned}
N(P_1)&=\{A\},\\
N(P_2)&=\{B,F_1\},\\
N(P_3)&=\{B,F_2\},\\
N(P_4)&=\{A,F_1,F_2,F_3,F_4,F_5\},\\
N(P_5)&=\{A,F_1,F_2,F_3,F_4,F_5\}.
\end{aligned}
\]
The plant degrees are \(1,2,2,6,6\), respectively. Direct application of the proved gain identity gives
\[
H_A(q)=1+2q^5,\quad H_B(q)=2q,\quad
H_{F_1}(q)=H_{F_2}(q)=q+2q^5,\quad
H_{F_3}(q)=H_{F_4}(q)=H_{F_5}(q)=2q^5.
\]
For every \(0<q<1\), \(H_A-H_{F_1}=H_A-H_{F_2}=1-q>0\), and \(H_A-H_{F_3}=H_A-H_{F_4}=H_A-H_{F_5}=1>0\). Hence the unique global optimum, away from ties, is either \(A\) or \(B\). Their score difference is
\[
f(q)=H_A(q)-H_B(q)=1-2q+2q^5.
\]
We have \(f(0)=f(1)=1>0\) and \(f(3/4)=-13/512<0\). Furthermore, \(f'(q)=-2+10q^4\) is strictly increasing on \((0,1)\); it vanishes once, so \(f\) first strictly decreases and then strictly increases. The intermediate value theorem now gives exactly two zeros \(\alpha<3/4<\beta\) in \((0,1)\). Target \(A\) is uniquely optimal on \((0,\alpha)\cup(\beta,1)\); target \(B\) is uniquely optimal on \((\alpha,\beta)\); and precisely \(A,B\) tie at the two switch points. This constructs the claimed reentry and proves sharpness in plant count.

## Verification

`verify.py` is a standalone Python 3 script using only the standard library. It independently evaluates the complete probability distribution of all \(2^7\) untreated pollinator-survival states and all \(2^6\) states when a chosen pollinator is guaranteed to persist. For \(q\in\{1/4,3/4,9/10\}\), it calculates each target's expected richness advantage from these state probabilities and confirms that the result is \(qH_j(q)\), using exact rational arithmetic for all seven targets. It also checks the explicit sign value \(f(3/4)=-13/512\). Run `python3 verify.py` in a directory containing both files.

These finite calculations verify the example and the gain formula at sampled probabilities; they are not a proof of the universal four-plant cutoff, which is established analytically above. The numerical switch-point approximations \(\alpha\approx0.5506065793\), \(\beta\approx0.7690997032\) are illustrative only; the exact definition is as the two roots of \(1-2q+2q^5\) in \((0,1)\).

## Relationship to prior work

Memmott, Waser and Price (2004) introduced influential qualitative plant–pollinator network removal experiments and highlighted redundant mutualists and the conservation importance of connected pollinators. Kaiser-Bunbury and collaborators (2010) analyzed extinction sequences, weighted links and interaction rewiring in observed pollination networks. Traveset, Tur and Eguíluz (2017) modeled stochastic coextinction with interaction dependencies. Bane, Pocock and James (2018) compared structural effects and knockout rules across models. None of the specifically inspected arguments or reported results establishes a four-versus-five plant threshold for reentry of the optimal **single guaranteed pollinator** under a common independent extinction probability. Existing qualitative claims that generalists matter, and the general mathematical concept of component reliability importance, do not by themselves imply the exact threshold and explicit reentrant witness established here. This is a statement about the inspected material, not a claim of exhaustive priority.

## Limitations

The claim is confined to the stated static binary dependency model with common independent pollinator failure probability, equal plant weights, equal intervention costs, a guarantee on one pollinator, and no secondary cascades or rewiring. The example is a mathematically admissible network, not an empirical description of any observed system. No minimality in the number of pollinators or edges is claimed. The universal theorem gives a necessary minimum plant count for reentry, not a bound on all possible ranking switches in larger networks. Specialized network-reliability literature could contain an equivalent theorem under another formulation; independent literature auditing remains desirable.

## References

1. Memmott, J., Waser, N. M. & Price, M. V., “Tolerance of pollination networks to species extinctions”, *Proceedings of the Royal Society B* (published online 6 December 2004), DOI 10.1098/rspb.2004.2909. https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
2. Kaiser-Bunbury, C. N., Muff, S., Memmott, J., Müller, C. B. & Caflisch, A., “The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour”, *Ecology Letters* (2010), DOI 10.1111/j.1461-0248.2009.01437.x. https://www.biochem-caflisch.uzh.ch/sites/default/files/publist/pdfs/smuff10.pdf
3. Traveset, A., Tur, C. & Eguíluz, V. M., “Plant survival and keystone pollinator species in stochastic coextinction models: role of intrinsic dependence on animal-pollination”, *Scientific Reports* (2017), DOI 10.1038/s41598-017-07037-7.
4. Bane, M. S., Pocock, M. J. O. & James, R., “Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness”, *Ecology and Evolution* (2018), DOI 10.1002/ece3.4529. https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.4529
