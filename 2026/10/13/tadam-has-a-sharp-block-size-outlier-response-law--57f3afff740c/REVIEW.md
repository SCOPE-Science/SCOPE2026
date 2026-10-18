# Independent mathematical audit

## correctness

PASS

Original TAdam Algorithm 1 and equations (8)–(10) use w(D)=(nu+d)/(nu+D) and W^+=((2beta-1)/beta)W+w. Set D=0 repeatedly: fixed point is W*=beta(nu+d)/[nu(1-beta)]. Substituting into w/(W*+w) cancels nu+d and yields exact (1-beta)nu/(nu+beta D). The displacement in V^-1 norm is (1-beta)nu sqrt(D)/(nu+beta D); derivative wrt sqrt(D) changes sign only at D=nu/beta. Default nu=d and D=kz² gives the half-threshold. Independent exact fraction substitutions gave blending 4/85 for beta=9/10,nu=2,d=10,D=5/2; 1/11 for beta=3/4,nu=3,d=2,D=7; and 3/8 for beta=5/8,nu=d=1,D=0. No full-optimizer stability claim.

## originality

PASS

Original Ilboudo–Kobayashi–Sugimoto TAdam arxiv2003.00179, Algorithm 1, states precisely the weight and pseudo-count recurrence, and discusses downweighting large Mahalanobis anomalies and coarse block limitations. The calculated fixed-point influence profile, sharp maximizing distance and k-versus-d threshold are not explicitly stated in inspected relevant pages. This is a quantitative sharpening of the published qualitative behavior, not a new optimizer. It is algebraically derivable from the published equations and may have been worked out in follow-up robustness work; originality is qualified.

## value

PASS

Robustness against sparse outlier coordinates is a central design question when parameter blocks are large. The sharp redescending gross-displacement bound and sqrt(d/k) detection threshold show quantitatively why sparse corruptions can escape a whole-vector Student-t gate while dense aberrations are downweighted; these are interpretable sensitivity diagnostics, not just re-labeled update equations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
