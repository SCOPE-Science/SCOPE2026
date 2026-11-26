# Independent mathematical audit

## correctness

PASS

The stable causal filter is integrable; its nonnegative, strictly positive on positive times impulse response in the overdamped and critically damped cases proves strict positivity by the double convolution. In the underdamped case put f=a0/m and D=(beta+k)^2+omega^2. Stationary balance gives E[V sigma]=k E[X sigma], D E[X sigma]=f, E[XV]=0 and 2 beta E[V^2]=f E[V sigma]. The V-X balance then gives the stated C(0), and conditioning on the future orientation gives the forced covariance ODE with C'(0)=0. Solving and dividing by A yields the displayed cosine and sine coefficients. At k=beta the ratio R/A is strictly below 1 for every omega>0. For q=k/beta<1 and x=(omega/beta)^2, the squared amplitude minus 1 has numerator F_q(x) over 4x(1+x) after cancellation; F_q decreases on x>0 and is negative at (1-q^2)/3. This covers the nonnegative sine coefficient. For the other case, b,h_*<0 and 0<-b<1, 0<-h_*<a; comparison on the first quadrant follows from the nonpositive derivative of exp(-a theta)(cos theta+a sin theta), on the second from a<exp(a theta) for theta>=pi/2, and the other two quadrants give strict bounds immediately. Periodicity proves the comparison for all lags. For k>beta, late cosine peaks and troughs give opposite signs. The first zero and the onset of negative values are bounded below by log(A/R)/(k-beta) near the threshold and above by that time plus one period. A trough exactly at the bound has negative derivative, so the upper bound also covers negativity. Smoothness of R/A at k=beta gives the claimed coefficient and O(1) remainder for either definition. Do not identify first zero and first sign-changing zero exactly: a negative-cosine lobe can touch zero at its strict interior minimum (at phase pi+arctan((k-beta)/omega) modulo 2pi), and then the earlier zero is tangential. This does not affect either asymptotic. The signed area follows by integrating the double convolution over the full line, using int h=Omega^(-2) and int exp(-k|t|)=2/k, then halving by evenness. The original checker was inspected, not run. Independent bounded replay /workspace/replay/1_delay.py recovered the example 23.69746138449596 and illustrates the possible tangency; finite examples are not the threshold proof.

## originality

PASS

Credit the oscillator/filter and its covariance formula as known at the level of matching second-order inputs. The distinct claim relative to checked earlier literature is the uniform sign boundary including its slow side and the singular delay law. There is verified equivalent catalogue coverage in a later-dated release, not independent evidence of earlier publication.

## value

PASS

It settles which underdamped active traps exhibit genuinely negative stationary memory, something not settled by damping alone. The precise positive boundary and the divergent lag at onset show why sign changes can be physically hard to observe just beyond the threshold, despite a positive signed area.

The dated certificate retains the supplied scientific assessment, sources and limitations.
