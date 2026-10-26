# Review of the scalar adaptive exponential Gaussian iteration

## Correctness

**PASS.** The exact scalar recurrence follows from the published Gaussian update. The logarithmic variable reduces it to a continuous, bounded-iterate clipped Ricker map with a unique fixed point. For \(H\le2\), any hypothetical two-cycle would have to cross zero, where its displacement \(\delta>0\) would obey both \(\delta\ge2\operatorname{artanh}(\delta/H)\) and \(2\operatorname{artanh}(\delta/H)>2\delta/H\ge\delta\), an impossibility. Coppel's interval convergence theorem then proves global covariance convergence. For \(H<2\) the mean factor tends into the open unit disk; for \(H\ge2\) the initial state \(s=1\) proves sharp failure of global joint attraction. Elementary maximizing-state algebra proves the exact independent \(H+\beta\) mean damping frontier. Critical Taylor expansions yield \(\sqrt n\) covariance and \(n^{-3/2}\) generic mean rates. The verifier passed 1,152 checks. The finite numerical checks supplement, not replace, the proof.

## Originality

**PASS, with historical priority uncertainty.** Che et al., arXiv:2601.14855, equations (12)–(15), Theorem 1 and relevant proof in Appendix A.1, prove the deterministic Gaussian claim under \(H\le1\), \(\beta\le1\); this does not imply global convergence for \(1<H<2\) or arbitrary \(\beta\), nor the distinct sharp \(H+\beta\) one-step mean criterion or critical mean oscillation/capture. Baigent et al. (2023) and their discussion of earlier Ricker results treat constant-parameter population maps, not the exact adaptive cap or the coupled variational mean recursion. Coppel's general no-two-cycle theorem is an explicitly acknowledged tool, not the new result. Actual mathematical-database and literature searches did not find an implication covering this combination. Specialized feedback-control or capped-Ricker literature may still contain equivalent statements; no absence-of-search-hit argument is treated as proof of priority.

## Mathematical value

**PASS.** The source theorem's small-step, small-cap restriction is practically restrictive for warm-up in Gaussian variational numerical integration. The result identifies a larger, sharp globally convergent region \(0<H<2\) independent of cap magnitude, and distinguishes it from the strictly smaller, exact nonexpansive-mean region \(H+\beta\le2\). This distinction predicts transient amplification in convergent runs. At the boundary the covariance can converge (and even reach its target in one step) while the mean oscillates forever; generic critically convergent means instead decay polynomially. The scope is a natural numerical method in its simplest identifiable model, not a claim about multidimensional or stochastic versions.

## Closest literature and limitations

Primary point of comparison: Baojun Che, Yifan Chen, Daniel Zhengyu Huang, Xinying Mao and Weijie Wang, *Adaptive Exponential Integration for Stable Gaussian Mixture Black-Box Variational Inference*, arXiv:2601.14855, first posted January 21, 2026. Classical comparator: Stephen Baigent et al., *A global picture for the planar Ricker map*, Journal of Difference Equations and Applications 29 (2023), 575–591, doi:10.1080/10236198.2023.2222855, particularly published pages 2–3. The interval-iteration theorem used is W. A. Coppel (1955), doi:10.1017/S030500410002990X. The findings are restricted to a deterministic scalar Gaussian target; exact matrix, noisy and coupled-mixture cases are not proved. Earlier specialized adaptive-feedback literature may change historical priority.

Self-review: passed. Independent audit: not yet performed.
