# Independent mathematical audit

## correctness

PASS

PASS: Stationarity requires x!=0 and y=2xz. Dividing the second equation gives z(1-x^2-z)=1, implying z<0 (z>0 would give x^2<0). With t=-z>0, x^2=1+t+1/t and nu=Phi(t)=t(t^2+t+5)/[5(t^2+t+1)]. Independent symbolic differentiation gives Phi'(t)=P(t)/[5(t^2+t+1)^2], P=t^4+2t^3-t^2+2t+5>0 for t>0, hence bijective onto nu>0 and two sign equilibria. Independently recomputed Jacobian characteristic coefficients a1=(1-4t^2)/(2t), a2=(15-17t-17t^2)/10, a3=2P/(5t). For 0<t<1/2 a1,a2,a3>0 but a1a2-a3=N/(20t)<0 (N=60t^4+52t^3-69t^2-33t-25), so two RHP roots. Since a3>0, no zero root; an imaginary root would require a3=a1*a2 and a2>=0, impossible both for t<1/2 and t>=1/2. The unstable index is thus identically two; the separate source necessary relations omit this stationarity condition.

## originality

PASS

PASS best of knowledge: The published paper presents plotted stable-node equilibria from only two necessary coordinate relations, not full simultaneous stationarity. Their reported branch is not an equilibrium of the printed equations. Exact sign threshold and universal index-two claim correct that source.

## value

PASS

PASS: A full real-parameter equilibrium threshold and universal hyperbolic unstable-index theorem correct a physically interpreted chaotic model's core local stability description, rather than merely adjusting numeric eigenvalues; it clarifies what claims about coexisting attractors do not follow.

The dated certificate retains the supplied scientific assessment, sources and limitations.
