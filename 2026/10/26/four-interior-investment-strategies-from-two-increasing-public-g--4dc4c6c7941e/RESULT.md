# Four interior investment strategies from two increasing public-good thresholds

## Finding
Consider the weak-selection pair-approximation adaptive dynamics for continuous public-goods investment on an infinite regular graph, as in [1]. For a benefit that is the **sum of two increasing, equally steep sigmoid returns**, with their thresholds equidistant from half of the maximal total contribution, the dynamics can have **exactly four distinct interior singular investments**, with two convergence-stable and evolutionarily stable strategies and two repellers. For a single sigmoid, the corresponding model has at most two interior singular strategies and only one attracting singular strategy [1].

The following characterization is necessary and sufficient. Define the normalized quantities
\[
 h=\tfrac{\beta}{2}(T_+-T_-),\quad H=\cosh h,\quad L=\tfrac{\beta n}{2},\quad Q=\cosh L,\quad \theta=\frac{nc}{(n+2)b\beta}.
\]
Assume \(n\ge4\), \(\omega,b,c,\beta>0\), and \(T_\pm=n/2\pm h/\beta\) with \(0<h<L\). **Precisely four distinct roots in \((0,1)\)** exist if and only if
\[
 \boxed{H>2,\qquad \max\left\{\frac1{1+H},\frac{1+HQ}{(H+Q)^2}\right\}<\theta<\frac{H^2}{4(H^2-1)}.}
\]
The four-root regime is possible only for threshold separation
\[
 \boxed{\beta(T_+-T_-)>2\operatorname{arcosh}(2).}
\]
Let
\[
 C_{\pm}=\frac{H(1-2\theta)\pm\sqrt{H^2-4\theta(H^2-1)}}{2\theta},
 \qquad 1<C_-<H-2/H<C_+<Q.
\]
Then, in increasing order, the four investments are
\[
 x_1=\frac12-\frac{\operatorname{arcosh}C_+}{\beta n},\quad
 x_2=\frac12-\frac{\operatorname{arcosh}C_-}{\beta n},\quad
 x_3=\frac12+\frac{\operatorname{arcosh}C_-}{\beta n},\quad
 x_4=\frac12+\frac{\operatorname{arcosh}C_+}{\beta n}.
\]
The first and third are repellers; the second and fourth are locally asymptotically attracting and also satisfy the evolutionary-stability Hessian test in [1, Eq. (B18)].

For example, take \(n=10\), \(\beta=c=1\), \(b=160/51\), \(h=\operatorname{arcosh}3\), and \(T_\pm=5\pm h\). Then \(\theta=17/64\), \(H=3\), \(C_\pm=(45\pm16\sqrt2)/17\), and the roots are approximately \(0.294224,0.422455,0.577545,0.705776\), with respective types repeller, attractor, repeller, attractor.

## Assumptions and scope
The population is infinite and occupies an undirected regular network of degree \(k=n-1\ge3\); mutations are rare, selection is weak, trait investment \(x\) lies in \([0,1]\), and the model uses death-birth updating and the pair approximation of [1]. We analyze the resulting **one-dimensional deterministic selection-gradient equation**, not the exact finite stochastic network or an arbitrary strong-selection limit. Benefits depend on a group's total investment \(s\) and costs are linear:
\[
 B(s)=b\left(\sigma(\beta(s-T_-))+\sigma(\beta(s-T_+))\right),\quad
 \sigma(t)=\frac1{1+e^{-t}},\quad C(x)=cx.
\]
In this regime [1, Eq. (B16)] supplies
\[
 \dot x=\frac{\omega(n-3)}{(n-2)n}\big((n+2)B'(nx)-nc\big).
\]
For scientific interpretation the two sigmoids represent successive beneficial project stages; unlike an increase-then-decrease self-poisoning response [2], the combined benefit remains strictly increasing. The sharp criterion refers to **four distinct interior zeros**; tangencies and endpoint zeros do not count. The formula for \(\theta\) normalizes the contribution cost by each sigmoid's amplitude and slope.

## Proof
Write \(z=\beta n(x-1/2)\), so \(-L\le z\le L\). With \(g(v)=\sigma(v)(1-\sigma(v))=1/(2+2\cosh v)\), direct differentiation yields
\[
 \frac{B'(nx)}{b\beta}=g(z+h)+g(z-h)
 =\frac{1+H\cosh z}{(H+\cosh z)^2}.
\]
For the last identity, put \(t=e^z\), \(u=e^h\); its left-hand side becomes \(tu/(1+tu)^2+tu/(t+u)^2\), while \(C=(t+t^{-1})/2\) and \(H=(u+u^{-1})/2\) give exactly the displayed rational expression after multiplying numerator and denominator by \(4t^2u^2\). Therefore, because the prefactor multiplying the selection gradient is positive, all its interior roots correspond to
\[
 F_H(C):=\frac{1+HC}{(H+C)^2}=\theta,\qquad C=\cosh z\in[1,Q].
\]
The derivative with respect to \(C\) is
\[
 F'_H(C)=\frac{H^2-2-HC}{(H+C)^3}.
\]
When \(H\le2\), it is nonpositive on \([1,Q]\) and strictly negative away from the endpoint in the borderline case, giving at most one distinct admissible \(C>1\) and hence at most two distinct interior investments. When \(H>2\), it is positive from \(C=1\) to \(C_*=H-2/H\) and negative thereafter. Since \(Q>H>C_*\), \(F_H\) has an interior maximum
\[
 F_H(C_*)=\frac{H^2}{4(H^2-1)},\quad
 F_H(1)=\frac1{H+1},\quad F_H(Q)=\frac{1+HQ}{(H+Q)^2}.
\]
Exactly two distinct \(C\)-roots strictly inside \((1,Q)\), one on each side of \(C_*\), occur exactly when \(\theta\) strictly exceeds both endpoint values and is strictly below the maximum. Each \(C>1\) gives two distinct \(z\)'s, hence four distinct interior \(x\)'s. Multiplying \(F_H(C)=\theta\) by \((H+C)^2\) produces the quadratic
\[
 \theta C^2+H(2\theta-1)C+\theta H^2-1=0,
\]
whose solutions are the displayed \(C_\pm\). This also shows there can never be more than four interior zeros for this benefit.

For root types, the selection gradient has the sign of \(F_H(\cosh z)-\theta\). At the four increasing zeros this sign alternates \(-,+,-,+,-\), so \(x_1,x_3\) are repelling and \(x_2,x_4\) are attracting, all hyperbolic. At \(x_2,x_4\) one has \(B''(nx)<0\); the linear cost has \(C''=0\). Therefore [1, Eq. (B18)] gives a strictly negative invasion-fitness curvature because its \(B''\)-coefficient \(n^3+9n^2-31n+19\) is positive for every integer \(n\ge4\): at \(n=4\) it equals \(103\), and its derivative \(3n^2+18n-31\) is positive for \(n\ge4\). Thus both attractors meet that paper's evolutionary-stability test. Finally \(H>2\) is equivalent to the stated sharp separation bound. All inequalities are strict precisely to exclude collisions and boundary crossings.

## Verification
The standard-library program `verify_two_threshold.py` evaluates \(B'(nx)/(b\beta)\) **directly as a sum of two sigmoid derivatives**, independently of the rationalized \(F_H\) formula, brackets and bisects every root on a 4096-step grid, checks root correspondence and signs on both sides, and verifies all four roots and their stability for the exact-parameter example plus 140 distinct randomly generated admissible parameter triples. Execute `python3 verify_two_threshold.py`; it prints the four example investments and a PASS count. These finite tests are corroboration, not the proof of the all-parameter equivalence.

## Relationship to prior work
Luo, Lin, Chen, and Szolnoki [1] establish the relevant pair-approximation adaptive gradient for arbitrary differentiable benefits and fully analyze the one-sigmoid specialization, which yields at most two singular strategies. The gradient equation itself is prior work. This result performs the previously unreported exact four-root and stability classification for a naturally distinct **sum of two increasing logistic thresholds**, including a sharp separation constant and necessary-and-sufficient cost window. A general theorem concerning mixtures of two logistic densities might subsume the bimodality lemma; the claimed contribution is the explicit public-goods investment phase diagram, not first discovery of mixture bimodality.

Archetti [2] derives broad shape constraints for **well-mixed binary** public-goods replicator games via Bernstein polynomials and discusses a "double inverse sigmoid" with benefits increasing and then decreasing. That construction and model are not the two increasing sigmoid stages under continuous-investment graph adaptive dynamics considered here. Analogies between their number of equilibria are acknowledged but are not identical results.

## Limitations
This is an exact theorem for a specified deterministic pair-approximation evolutionary equation, not a proof of convergence in finite stochastic populations or of robustness to arbitrary asymmetric sigmoids. The strict parameter inequalities omit nongeneric tangency and boundary-root classifications. The ratio of benefit to cost may lie in a specified range; the result is not a universal claim that two stages always create four singular strategies. Possible equivalent calculations in earlier work on two-component logistic-density mixtures and other adaptive dynamics remain a publication-priority risk. No independent scientific audit has been performed.

## References
[1] Jing Luo, Duozi Lin, Xiaojie Chen, and Attila Szolnoki, "Evolutionary dynamics of continuous public goods games in structured populations," *Chaos* 35, 043115 (2025), arXiv:2504.06769, https://arxiv.org/abs/2504.06769. First publicly posted 2025-04-09. Eq. (B16) gives the selection gradient; Eqs. (B17)-(B18) give stability tests; Eqs. (B21)-(B24) address the single sigmoid.

[2] Marco Archetti, "How to Analyze Models of Nonlinear Public Goods," *Games* 9, 17 (2018), https://doi.org/10.3390/g9020017. Sections 2.4 and 2.6, especially the different double-inverse-sigmoid construction in Eq. (13).
