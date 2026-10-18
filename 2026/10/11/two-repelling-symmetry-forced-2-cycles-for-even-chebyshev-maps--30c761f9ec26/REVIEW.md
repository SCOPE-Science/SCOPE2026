# Independent mathematical audit

## correctness

PASS

Recomputed from actual RESULT.md and verify.py: substitute y=x^n and clear positive denominator to obtain E_n(y)=(n+1)(4n^2+5n+2)y^3+2(n+1)(4n+3)y^2+(-n^2+7n+6)y+2. Independent SymPy discriminant exactly 4n^6(n+1)(4n^2-63n-59)>0 on n>=18; coefficient signs show exactly one negative and two positive simple roots. The source critical-value inequality Q_n(c)<-c separates the positive solutions. At smaller root E_n'<0 so Q_n'<-1. For outer root H=n y E_n'-4((n+1)y+1)^3 controls Q_n'-1; independent resultant is 8n^9(n+1)^2(16n^4-216n^3-815n^2-931n-356) and quartic is positive for n>=18. At n=18, E(1/28)=-113/5488<0, E(1/27)=2720/19683>0, H(1/28)=293023/5488>0 and H' increases on bracket. Continuous outer branch cannot cross multiplier +1, so Q_n'(x_+)>1. Oddness squares Q_n' for 2-cycle; neither is attracting or parabolic. Exact polynomial checks do not prove other periods/nonreal cycles absent.

## originality

PASS

The original Nayak--Phogat manuscript constructs only the inner centrally symmetric two-cycle and labels it the closest in its table. The audited global two-root exhaustion and strict repelling inequalities are not established by that original claim; the second branch and uniform outer multiplier need a cubic/resultant argument. Similar Chebyshev symmetry papers treat other families. Searches for Q_n(x)=-x and invariant-line multipliers found no equivalent pre-existing theorem. Best-of-knowledge with explicit recent-preprint risk.

## value

PASS

The motivating 2026 dynamical investigation leaves convergence for even n>=18 open; the theorem removes the precise centrally symmetric real period-two candidates from its attracting-obstruction list on every invariant critical line. This is a natural exhaustive dynamical boundary result rather than a numerical orbit sample; it does not solve general convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
