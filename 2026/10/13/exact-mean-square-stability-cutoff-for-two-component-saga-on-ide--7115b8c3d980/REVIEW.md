# Independent mathematical audit

## correctness

PASS

With f1=f2=L*x^2/2, s=eta*L, old cached table mean u and half-difference v, fresh fair sign sigma, standard SAGA has x'=(1-s)x+s*sigma*v, u'=(x+u-sigma*v)/2, v'=(v+sigma*(x-u))/2. The explicit quadratic V_s=(s+2)x^2/s+s(s+1)u^2+3s(s+1)v^2-2s*x*u is positive definite for every s>0 (leading coefficient (s+2)/s>0, x/u minor 3s+2>0, v coefficient 3s(s+1)>0). Independent exact symbolic expansion reproduces E[V_s(next)|state]-V_s(state)=(3s^2-4)x^2. For 0<s<2/sqrt(3), telescope negative drift to obtain sum_k E[x_k^2]<infty, hence E[x_k^2]->0; each cache second moment obeys half-old+half-E[x_k^2], hence also tends to zero. At s>=2/sqrt(3), energy is a nondecreasing nonnegative process in expectation, bounded below by V_s(initial)>0 for every nonzero deterministic state. Hypothetical E[x_k^2]->0 forces the cache moments and E[V_s] to zero, contradiction. This is an exact all-init mean-square iff result, not proof of almost-sure divergence. Finite algebra check independently verified the general symbolic identity; proof addresses arbitrary deterministic cache initialization.

## originality

PASS

Defazio–Bach–Lacoste-Julien define standard SAGA and give conservative convergence stepsizes; Gazagnadou–Gower–Salmon study optimized sufficient stepsizes for broader settings; Taylor–Van Scoy–Lessard explore general Lyapunov certificates. The present 2-component identical-quad exact 2/sqrt(3) iff threshold and conserved critical energy do not follow from those general guarantees in inspected sections. The related previously published two-client Loopless SVRG frontier is a different algorithm. A prior exact SAGA mean-square calculation in control literature remains a risk.

## value

PASS

Even zero component heterogeneity does not equate SAGA to deterministic gradient descent, because separate cached evaluation points create stochastic memory error. The exact sharp stability interval (0,2/sqrt(3)) versus GD (0,2), and positive-definite critical energy, are nontrivial boundaries with relevance for step-size and table initialization analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
