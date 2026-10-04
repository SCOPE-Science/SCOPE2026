# The combined manual–digital contact-tracing threshold region is coordinatewise monotone
## Finding
For the Britton–Zhang limiting SIR epidemic with instantaneous iterative manual and digital contact tracing, fix \(\beta,\gamma,\delta>0\) and let \(R_{\mathrm{DM}}(p,\pi)\) be the paper's component reproduction number. If \(0\le p_1\le p_2\le1\) and \(0\le\pi_1\le\pi_2\le1\), then
\[
R_{\mathrm{DM}}(p_1,\pi_1)\le1\ \Longrightarrow\ R_{\mathrm{DM}}(p_2,\pi_2)\le1,
\qquad
R_{\mathrm{DM}}(p_2,\pi_2)>1\ \Longrightarrow\ R_{\mathrm{DM}}(p_1,\pi_1)>1.
\]
Consequently the subcritical set \(\{(p,\pi):R_{\mathrm{DM}}(p,\pi)\le1\}\) is coordinatewise upper, and the threshold functions \(\pi_c(p)=\inf\{\pi:R_{\mathrm{DM}}(p,\pi)\le1\}\) and \(p_c(\pi)=\inf\{p:R_{\mathrm{DM}}(p,\pi)\le1\}\) are nonincreasing. Thus the level-one threshold frontier is monotone even though \(R_{\mathrm{DM}}\) itself can be non-monotone away from level one.

This supplies the order statement left open in Britton and Zhang's discussion of the combined tracing model. Their simulations show that the component reproduction number itself need not decrease monotonically in either tracing parameter, but they observed a monotone-looking \(R_{\mathrm{DM}}=1\) curve and stated that a proof was missing. The distinction is essential: the theorem concerns only which side of the branching-process threshold a parameter pair lies on.

## Assumptions and scope
The object is exactly the limiting combined process \(E_{\mathrm{DM}}(\beta,\gamma,\delta,p,\pi)\) in Britton and Zhang, with homogeneous mixing, independent app adoption, instantaneous manual and digital tracing, recursive tracing, and the paper's convention that infected contacts who have recovered naturally can still be identified and propagate tracing. The rates satisfy \(\beta,\gamma,\delta>0\), and \(p,\pi\in[0,1]\).

Each potential infected individual has an app mark \(U\sim\mathrm{Unif}(0,1)\), so it is an app user at level \(\pi\) exactly when \(U\le\pi\). Each potential infection edge has an independent manual-tracing mark \(V\sim\mathrm{Unif}(0,1)\), so it is manually traceable at level \(p\) exactly when \(V\le p\). An infection edge is therefore traceable when
\[
V\le p\quad\text{or}\quad(U_{\rm parent}\le\pi\ \text{and}\ U_{\rm child}\le\pi).
\]
For coordinatewise larger \((p,\pi)\), the set of traceable infection edges is a superset.

The conclusion does not say that \(R_{\mathrm{DM}}(p,\pi)\) is numerically nonincreasing; the source explicitly exhibits numerical non-monotonicity away from level one. It also does not assert strictness, differentiability, or uniqueness of a level set beyond the threshold functions defined by the subcritical region.

## Proof
Use one common graphical construction for two parameter pairs \(\theta_1=(p_1,\pi_1)\le\theta_2=(p_2,\pi_2)\). Before tracing is imposed, assign every potential individual its app mark, natural-recovery clock, spontaneous-diagnosis clock, and rate-\(\beta\) potential infection-contact process; assign every potential infection edge its manual-tracing mark. These marks are independent. The total potential infection rate is \(\beta\) in both models, so changing \(\pi\) only changes app labels, not the contact clock. Let \(T_1\subseteq T_2\) be the resulting traceable-edge sets.

We first prove a deterministic pruning lemma: for a fixed realization of all clocks and marks, every infection realized under \(T_2\) is also realized under \(T_1\), at the same infection time. Suppose not, and let \(t\) be the first potential birth that occurs under \(T_2\) but not under \(T_1\). Its parent \(x\) is infectious under \(T_2\) immediately before \(t\), but not under \(T_1\). Natural recovery and the parent's own spontaneous-diagnosis clock are common, so under \(T_1\) the parent must have been removed earlier, at some time \(s<t\), by recursive tracing initiated by a spontaneous diagnosis at an infected vertex \(y\).

At time \(s\), \(x\) and \(y\) lie in the same \(T_1\)-traceable component of the realized infection tree. Follow the unique infection-tree path from \(x\) to \(y\). Every edge on that path belongs to \(T_1\), hence to \(T_2\). Starting from \(x\), every successive vertex on the path must already have been realized under \(T_2\): an ancestor is necessary for the existence of \(x\); and if the next vertex is a child, its parent cannot have ceased being infectious under \(T_2\) before that child's birth while leaving \(x\) present later. Indeed, if such a parent had been traced earlier, the already existing \(T_2\)-traceable path toward \(x\) would have removed the relevant ancestral branch; if the path toward \(x\) had not yet been born, removal of that parent would prevent it from being born later. Induction along the finite path therefore shows that \(y\) is realized under \(T_2\).

The vertex \(y\) is infectious under \(T_1\) at \(s\). It cannot have recovered earlier under \(T_2\), because its recovery clock and infection time are common. Nor can it have been traced earlier under \(T_2\): the same path argument would then either already remove \(x\) or prevent the later ancestry leading to \(x\), contradicting that \(x\) is infectious under \(T_2\) just before \(t\). Thus the same spontaneous-diagnosis clock of \(y\) fires at \(s\) in the \(T_2\) process. Since every edge of the \(T_1\)-traceable path from \(y\) to \(x\) is also in \(T_2\), recursive tracing removes \(x\) under \(T_2\) at time \(s\), again contradicting its being infectious at \(t\). The assumed first discrepant birth cannot exist. Hence the ever-infected set under \(\theta_2\) is pathwise contained in that under \(\theta_1\).

It follows that the event that the limiting epidemic grows without bound under \(\theta_2\) is contained in the corresponding event under \(\theta_1\). Britton and Zhang's Corollary 2 and its proof identify the survival threshold of the two-type component branching process: the limiting process dies out almost surely when \(R_{\mathrm{DM}}\le1\), and grows beyond all limits with positive probability when \(R_{\mathrm{DM}}>1\). Therefore
\[
R_{\mathrm{DM}}(p_2,\pi_2)>1\Longrightarrow R_{\mathrm{DM}}(p_1,\pi_1)>1,
\]
and the contrapositive gives the subcritical implication in the finding.

Finally, \(p=1\) makes every infection edge manually traceable, so no new component is born and the component mean-offspring matrix is zero. Likewise, at \(\pi=1\) every realized app-to-app transmission is digitally traceable and the only reachable component type creates no untraced offspring; the spectral threshold from the reachable class is zero. Hence the subcritical set is nonempty on every horizontal and vertical section, so the two infimum threshold functions are well defined and their nonincreasing order follows immediately from coordinatewise upperness.

## Verification
The proof was checked directly against the source's combined-model rules: manual links are independent with probability \(p\); app status is independent with probability \(\pi\); diagnosis recursively traces parents and descendants along traceable links; naturally recovered infected contacts remain tracing conduits; and the source proves that \(R_{\mathrm{DM}}\) has the extinction/survival threshold at one.

The included `verify.py` performs two finite sanity checks. First, it exhaustively checks monotonicity of the edge-traceability predicate on a rational parameter grid. Second, on finite potential infection trees with recursive tracing and recovered intermediates, it exhausts nested trace-edge subsets and verifies that stronger tracing never realizes an infection absent under weaker tracing. These finite checks are not used as an infinite proof; the analytic earliest-discrepant-birth argument above supplies that step.

## Relationship to prior work
Britton and Zhang derive the combined two-type component branching process and prove that \(R_{\mathrm{DM}}>1\) is equivalent to positive-probability unbounded growth, whereas \(R_{\mathrm{DM}}\le1\) gives extinction. Their numerical Section 6.3 shows that \(R_{\mathrm{DM}}\) itself can be non-monotone in \(p\) and \(\pi\), but the \(R_{\mathrm{DM}}=1\) contour appears monotone; Section 7 explicitly says that a proof is missing. The result here supplies exactly that missing threshold-order statement by coupling the underlying tracing graph rather than differentiating the component reproduction number.

A related Zhang–Britton SEIR network model with delayed, one-step, forward-only tracing reports numerical monotonicity of its different reproduction number in app uptake and manual reporting probability. It does not cover the instantaneous recursive homogeneous-mixing model considered here or prove this level-one threshold order. Earlier manual-tracing branching-process literature establishes threshold criteria for other tracing mechanisms but does not state the coordinatewise combined manual/digital result proved here.

## Limitations
The theorem is specific to the source's idealized instantaneous and recursive tracing rules. Delays, imperfect digital registration, fatigue, one-step tracing, structured contacts, or parameter changes that alter the infection-contact process itself can break the graphical nesting used in the proof. No claim is made about the numerical monotonicity of \(R_{\mathrm{DM}}\), the shape or smoothness of its noncritical level sets, late-epidemic final sizes, or finite-population stochastic ordering after susceptible depletion.

## References
1. T. Britton and D. Zhang, “Epidemic models with digital and manual contact tracing,” *Advances in Applied Probability* 57 (2025), 1430–1455. DOI: 10.1017/apr.2025.15. Published online 2025-06-09.
2. D. Zhang and T. Britton, “An SEIR network epidemic model with manual and digital contact tracing allowing delays,” *Mathematical Biosciences* 374 (2024), 109231. DOI: 10.1016/j.mbs.2024.109231; arXiv:2402.13392.
3. F. G. Ball, E. S. Knock, and P. D. O'Neill, “Threshold behaviour of emerging epidemics featuring contact tracing,” *Advances in Applied Probability* 43 (2011), 1048–1065. DOI: 10.1239/aap/1324045698.
4. M. T. Barlow, “A branching process with contact tracing,” arXiv:2007.16182 (2020).
