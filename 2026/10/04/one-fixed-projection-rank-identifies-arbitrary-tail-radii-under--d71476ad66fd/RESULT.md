# One fixed projection rank identifies arbitrary-tail radii under approximate conditional isotropy

## Finding
Let \(p/N\to c\in(0,\infty)\), let \(\nu\) be an arbitrary probability measure on \([0,\infty)\), and let \(x_p\in\mathbb R^p\) admit a radial reduction \((\mathcal H_p,\rho_p)\) satisfying
\[
\rho_p\Rightarrow\nu,
\qquad
\frac1p\left\|\mathbb E[x_px_p^{\mathsf T}\mid\mathcal H_p]-\rho_p I_p\right\|_1\xrightarrow{P}0.
\]
Fix any \(\alpha\in(0,1)\), set \(q_p=\lfloor\alpha p\rfloor\), and for a rank-\(q_p\) projection \(P\) let \(S_P\) denote the sample covariance of the projected observations. Assume that for every deterministic rank-\(q_p\) projection sequence \(P_p\),
\[
\operatorname{ESD}(S_{P_p})\Rightarrow\mu_{c\alpha,\nu}
\]
weakly in probability. Then, with \(R_p=\|x_p\|^2/p\),
\[
R_p-\rho_p\xrightarrow{P}0,
\qquad
R_p\Rightarrow\nu,
\]
and the radial quadratic-form condition holds. Equivalently, for every deterministic uniformly bounded matrix sequence \(A_p\),
\[
\frac{{x_p^{\mathsf T}A_px_p}}{{p}}-R_p\frac{\operatorname{tr}A_p}{p}\xrightarrow{P}0.
\]
It follows that every deterministic proportional-rank projected sample covariance obeys the corresponding radial Marchenko--Pastur law. In particular, approximate conditional isotropy makes one fixed rank fraction sufficient to recover an arbitrary-tail parent radius law; no moment assumption on \(\nu\) is needed.

## Assumptions and scope
The vectors are real. The sample consists of independent copies of \(x_p\), with \(p/N\to c\in(0,\infty)\). Approximate conditional isotropy is exactly the trace-norm radial-reduction condition displayed above. The spectral hypothesis is required for every deterministic orientation of one rank fraction \(\alpha\in(0,1)\); a single orientation is not enough. The target \(\nu\) may have infinite first, second, or logarithmic moments.

The conclusion is a one-rank strengthening of the conditional-isotropy alternative in Xie, not a solution of arbitrary-tail radius identification without structural assumptions. It does not remove approximate conditional isotropy, and it does not claim that one projected covariance matrix at one orientation identifies the radius.

## Proof
Write
\[
R_{P,p}=\frac{\|P x_p\|^2}{q_p}.
\]
The first ingredient is the fixed-rank part of the conditional argument in Xie. Inspecting Steps (i)--(iv) of the proof of Theorem 9.3 shows that the argument is rank-by-rank: for any deterministic projection sequence with \(q_p/p\to\alpha\in(0,1]\), the spectral convergence at that sequence together with the radial-reduction hypothesis implies
\[
R_{P,p}-\rho_p\xrightarrow{P}0. \tag{1}
\]
The proof does not use spectral information at any other rank until after this statement is obtained. In the published argument the all-ranks assumption is then used with \(P=I_p\) to identify \(R_p\). Here that identity-rank step is replaced by Haar randomization.

Because (1) holds for every deterministic rank-\(q_p\) sequence, it holds uniformly over all such deterministic projections. Indeed, if for some \(\varepsilon>0\) the supremum of \(\Pr(|R_{P,p}-\rho_p|>\varepsilon)\) did not tend to zero, a violating deterministic sequence could be selected along a subsequence and completed arbitrarily off that subsequence, contradicting (1). The relevant probability is Borel in \(P\), so the same uniform bound applies to an independent Haar-uniform rank-\(q_p\) projection \(U_p\). Therefore
\[
\frac{\|U_px_p\|^2}{q_p}-\rho_p\xrightarrow{P}0. \tag{2}
\]

For a fixed nonzero vector, Haar invariance gives
\[
B_p:=\frac{\|U_px_p\|^2}{\|x_p\|^2}
\sim \operatorname{Beta}\!\left(\frac{q_p}2,\frac{p-q_p}2\right).
\]
The conditional law of \(B_p\) does not depend on \(x_p\), so on an enlarged probability space it can be taken independent of \((x_p,\rho_p)\). On \(\{x_p=0\}\) define the same independent beta variable; the identity below is unchanged because \(R_p=0\). Put
\[
A_p=\frac p{q_p}B_p.
\]
Then
\[
\mathbb E A_p=1,
\qquad
\operatorname{Var}(A_p)=\frac{2(p-q_p)}{q_p(p+2)}\longrightarrow0,
\]
so \(A_p\xrightarrow{P}1\), and (2) is exactly
\[
R_pA_p-\rho_p\xrightarrow{P}0. \tag{3}
\]
Since \(\rho_p\Rightarrow\nu\), the sequence \((\rho_p)\) is tight. Equation (3) and \(A_p\xrightarrow{P}1\) imply tightness of \((R_p)\): on \(\{A_p\ge1/2\}\),
\[
R_p\le2\bigl(|R_pA_p-\rho_p|+\rho_p\bigr).
\]
Hence \(R_p(1-A_p)\xrightarrow{P}0\), and
\[
R_p-\rho_p=(R_pA_p-\rho_p)+R_p(1-A_p)\xrightarrow{P}0.
\]
Slutsky's theorem gives \(R_p\Rightarrow\nu\).

At this point the hypotheses of Xie's moment-free one-rank characterization are satisfied: the actual parent radius now converges to \(\nu\), and the same fixed-rank spectral hypothesis holds for every deterministic orientation. That characterization therefore yields the radial quadratic-form condition. Its forward implication then gives the radial Marchenko--Pastur law at every proportional rank. This completes the proof.

## Verification
The critical source statements were checked in the full text of arXiv:2609.08328v1. Definition 9.2 is the radial-reduction/approximate-conditional-isotropy hypothesis. In the proof of Theorem 9.3, equation (9.8) is obtained for an arbitrary chosen proportional projection from its own spectral convergence; the next paragraph explicitly uses \(P=I_p\) to recover the parent radius. Thus the only missing bridge from one fixed rank to the parent radius is precisely the step supplied above. The same paper's Lemma 3.1 records the deterministic-sequence-to-uniform selection principle, and Theorem 2.3 is the moment-free one-rank characterization used after radius recovery.

The Haar calculation is exact. If \(G_1\sim\chi^2_{{q_p}}\) and \(G_2\sim\chi^2_{{p-q_p}}\) are independent, then \(B_p=G_1/(G_1+G_2)\) has the displayed beta law. Its standard mean and variance give the displayed formulas for \(A_p\), in particular variance of order \(p^{-1}\). No numerical experiment is used as a substitute for the asymptotic proof.

## Relationship to prior work
Xie proves three nearby results. Theorem 2.3 shows that one fixed rank fraction characterizes the radial quadratic-form condition when the actual parent radius law \(R_p\Rightarrow\nu\) is already known. Theorem 2.4 can recover an unknown radius from one-rank spectra under a small-subspace condition when the limiting spectral law has finite second moment; the paper explicitly leaves arbitrary-tail radius identification open. Theorem 9.3 permits arbitrary tails under approximate conditional isotropy and recovers \(R_p\Rightarrow\nu\), but assumes the radial Marchenko--Pastur conclusion at every proportional rank and uses the identity rank to recover the parent radius.

The present statement combines the rank-local part of Theorem 9.3 with a Haar projection identity to remove that identity-rank input. It therefore reduces the conditional-isotropy spectral hypothesis from every proportional rank to every orientation of one fixed proportional rank while retaining arbitrary tails. The classical isotropic characterization of Yaskov requires projected Marchenko--Pastur behavior over proportional rectangular projections and concerns a concentrating radius; it does not state the arbitrary radial-law conclusion here.

## Limitations
Approximate conditional isotropy remains a substantive structural assumption. The result does not settle arbitrary-tail radius identification in the unrestricted setting of Xie's Theorem 2.4. All orientations at the chosen fixed rank are still required. The proof is asymptotic and qualitative; it does not provide a finite-dimensional rate for radius recovery. The originality claim is the hypothesis reduction and arbitrary-tail radius-recovery bridge, not the classical beta law for Haar projections, the radial Marchenko--Pastur law itself, or the rank-local conditional resolvent argument from the source paper.

## References
1. Xiaohui Xie, *Radial Marchenko--Pastur laws: projection characterizations and rigidity*, arXiv:2609.08328v1, 2026. Relevant items: Theorems 2.3, 2.4, 9.3; Lemma 3.1; Definition 9.2; equation (9.8).
2. Pavel Yaskov, *The necessary and sufficient conditions in the Marchenko--Pastur theorem*, arXiv:1511.02711, 2015. Relevant item: Theorem 3.3.
