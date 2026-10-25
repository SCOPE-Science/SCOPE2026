# Independent mathematical audit

## correctness

PASS

Proof reconstructed from the actual frozen RESULT.md and the corresponding Xie source, not from source verifier claims. For any fixed deterministic rank q=floor(alpha p) projection sequence P, spectral convergence and conditional isotropy imply R_{P,p}=||Px_p||^2/q satisfies R_{P,p}-rho_p ->P0 via Xie Theorem 9.3 rank-local proof Steps (i)-(iv) to Eq. (9.8). Because that holds for every deterministic orientation sequence, a violating sequence would contradict it, hence the deviation probabilities converge uniformly over the deterministic rank-q Grassmannian. A Haar-uniform rank-q projection U independent of (x_p,rho_p) is therefore allowed. Conditional Haar B=||Ux||^2/||x||^2 follows Beta(q/2,(p-q)/2), with the zero-vector case handled by an auxiliary B; A=(p/q)B has mean 1 and variance 2(p-q)/(q(p+2)) ->0. Thus R_p A-rho_p ->P0. Since rho_p=>nu on [0,infinity) is tight, R_p is tight via P(A>=1/2)->1; hence R_p(A-1)->P0 and R_p-rho_p ->P0, giving R_p=>nu without any moment assumption. Xie Theorem 2.3 can now be invoked with its actual radius premise proved, yielding RQC and all-proportional-rank spectral consequences. The exact assumptions are real vectors, independent sample columns, p/N->c>0, alpha strictly between 0 and 1, EVERY deterministic orientation at this rank, and the normalized conditional trace-norm ACI property. No finite experiment is substituted for an infinite proof.

## originality

PASS

Best-of-knowledge PASS for the exact one-rank/all-orientations, ACI, arbitrary-tail radius-recovery implication, not for the ingredients. The full primary source Xie arXiv:2609.08328v1 provides fixed-rank spectral characterization only given the actual radius law (Theorem 2.3), unknown-radius recovery at a fixed rank under an extra second-moment condition (Theorem 2.4), and arbitrary-tail ACI recovery assuming every proportional rank (Theorem 9.3). Its proof of Theorem 9.3, Steps (i)-(iv) through (9.8), is rank-local but then invokes the identity rank P=I to recover the parent radius. The audited result adds a distinct deterministic-orientation-to-Haar transfer and the moment-free normalized beta concentration/tightness bridge, removing the identity-rank assumption. A very short corollary of existing proof techniques may be folklore; searches and full primary inspection identified no already stated or logically dominating one-rank ACI arbitrary-tail theorem. The conclusion is conditional on ACI and all orientations, and no claim to solving unrestricted arbitrary-tail identification is made.

## value

PASS

The one-rank arbitrary-tail radius-recovery problem is mathematically motivated by the gap between Xie Theorems 2.3, 2.4, and 9.3: knowing the parent radius is unnecessary under ACI if every orientation of one fixed rank is spectrally controlled. Removing an all-proportional-ranks hypothesis while preserving unknown potentially infinite-moment radial laws is an exact structural strengthening useful in conditional-isotropy/elliptical random-matrix models. The substantive content is rank-to-parent-radius recovery and hypothesis reduction, not a novel beta distribution or generic concentration result. Although concise, this bridges a natural precise quantifier/assumption gap and requires a nontrivial use of the source rank-local argument and Haar transfer; no downstream theorem or paper-size requirement is imposed. The result makes no stronger claim about all random vectors or about quantitative finite-size rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
