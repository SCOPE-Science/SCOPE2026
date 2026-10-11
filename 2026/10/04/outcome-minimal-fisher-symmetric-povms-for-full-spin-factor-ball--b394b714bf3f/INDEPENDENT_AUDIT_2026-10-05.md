# Independent mathematical audit

## correctness

PASS

The Clifford anticommutation equations give the SLD metric \(J_\theta=(I-\theta\theta^{\mathsf T})^{-1}\). The displayed biased simplex has positive probabilities, mean \(\theta\), and covariance \((1-\|\theta\|^2)I/d\). Transporting it by the score ellipsoid maps every support point to the effect-positivity boundary, so each \(M_i=a_iI+\gamma(b_i)\) is positive and the effects sum to identity. Their local probabilities are \(p_i\), score vectors are \(\ell_i\), and their covariance gives exactly \(F_\theta=J_\theta/d\). For any finite classical outcome model, \(\sum_i p_is_i=0\), so \(m\) positive-probability scores span dimension at most \(m-1\); full-rank \(d\)-dimensional Fisher information therefore requires \(m\ge d+1\). The construction attains equality.

## originality

PASS

Yamagata’s September 2026 primary paper gives the exact normalized attainable Fisher region and an explicit realization by randomized spectral SLD measurements, but its accessible primary statement does not give the sharp local support size \(d+1\) or a simplex compression. A separate April 2026 support-size paper gives only a much larger general upper bound \((\dim\mathcal H)^2+d(d+1)/2-1\). Fresh Resultary and web searches for spin-factor, Fisher-symmetric, simplex and outcome-minimal formulations did not find an arbitrary-interior \(d\ge4\) theorem matching both the construction and lower bound. The exact September paper’s full text was attempted first through public arXiv/OA routes; those routes did not yield the body, and the single authorized institutional fallback returned worker unavailable, so this remains an explicit originality risk rather than negative evidence.

## value

PASS

Exact measurement support is an independently motivated resource question in quantum estimation. The result provides a constructive optimum at every interior point and a matching information-rank lower bound, reducing the natural isotropic spin-factor implementation to the smallest possible alphabet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
