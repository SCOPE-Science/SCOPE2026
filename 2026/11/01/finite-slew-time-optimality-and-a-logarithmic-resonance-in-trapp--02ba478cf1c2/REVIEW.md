# Independent mathematical audit

## correctness

PASS

Itô gives y_dot=D1/tau-(tau^{-1}+mu a)y and x_dot=-2mu a x+2(D+y). Endpoint-independent slew and amplitude imply every admissible a(t)<=min(ai+Rt,af)=a*(t), even nonmonotone controls. Subtracting y equations yields a positive Volterra integral of (a*-a)y*, and subtracting x equations yields a positive integral of the y difference plus (a*-a)x*: hence x>=x*>xf and y>=y*>yf, with strictness unless protocols agree a.e. Derivative integrating factors show E*(t) strictly decreases; endpoint forces T>=t_R; threshold forces T>=t_eps; ramp-hold attains max. On holding, delta_y=delta_y0 exp(-ell s), delta_x=delta_x0 exp(-m s)+2delta_y0(exp(-ell s)-exp(-m s))/(m-ell), and at m=ell it is (delta_x0+2delta_y0 s)exp(-ms). For fixed physical parameters, m<ell,m>ell and critical m=ell yield the claimed sharp times, and the critical inversion ms-log(ms)=log(2dy/(m eps))+o(1) has an authentic loglog term. Independently solved the ramp ODE by SciPy and optimized the specified benchmark, obtaining T=1.71582033156873 versus 1.715820331569 in the source.

## originality

PASS

Best-knowledge new sharp finite-slew reachability result; same AOUP covariance equations and step response were known from Casert–Whitelam, not claimed new. Generic positive-system order principles might imply the ramp bound, but no prior source found combining exact endpoint reachability and resonant asymptotics. Avoid attributing standard comparison method to the new work.

## value

PASS

Finite actuator slew is a physically motivated constraint absent from the fast-step benchmark. Exact minimum time under arbitrary nonmonotone admissible competing protocols is a useful reachability fact, and the logarithmic resonance reveals a concrete Jordan-forcing slowdown at a natural parameter coincidence. It is narrow but structural and not a numerical protocol fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
