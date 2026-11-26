# Independent mathematical audit

## correctness

PASS

Direct linearization at a=g(E)>0 gives v_t=-a(v_x+kappa v), since u_E'+kappa u_E=0, with v(t,0)=b m(t), b=-Bg'(E)/a^2 and m=integral v. Scaling time by a gives after transit the stated truncated exponential renewal equation and 1-R(1-e^-k)=h'(E)/a. For R<=0 the shifted characteristic equation cannot have a root with Re s>=0 by the modulus bound. For subcritical R>0 the integral modulus is bounded by R(1-e^-k)<1; for supercritical R>0 the real integral decreases strictly to zero and yields a positive root. At equality the unmultiplied characteristic function has nonzero derivative at zero. At s=i omega the real and imaginary equations, for R>0, force (k omega)(e^k-cos(k omega))=k sin(k omega), impossible for omega nonzero since e^k-1>k. The root s=-1 introduced by clearing the denominator is not used. On L1 the transport semigroup is eventually compact: after one transit v(sigma,x)=b e^(-kappa x)m(sigma-x), and differentiation of the integral in moving-endpoint coordinates gives m'=(b-kappa)m-b e^(-kappa L)m(sigma-L). Finite-time mass bounds from the characteristic Volterra equation give equi-Lipschitz profiles after two transits. Thus exclusion of closed-right-half-plane roots gives exponential decay of the full linearized evolution, not only of a formal mode. The example independently follows from h(3/5+x)=21/125+x^3-2x/25, with extrema x=±sqrt(6)/15 and central roots x=0,±sqrt(2)/5. The equal-slope case is neutral in the spectral sense stated, not positive-real instability; no nonlinear basin follows. Frozen verify.py was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the joint spectral classification for the specified finite, absorbing, fixed-flux model, particularly exclusion of nonzero imaginary roots for unrestricted real feedback and the corresponding classified example. The scalar equilibrium closure, generic stationary folds, conversion by characteristics, and general delay methods are not separately original.

## value

PASS

The result converts a stationary fold diagnostic into a complete linear criterion for a natural, finite-residence subclass. In particular the imaginary-root exclusion for any real feedback is useful beyond calculating three stationary roots and prevents mistaking the distributed memory in this subclass for a mechanism of oscillatory linear destabilization. The classified example illustrates the distinction; it does not claim nonlinear hysteresis dynamics or basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
