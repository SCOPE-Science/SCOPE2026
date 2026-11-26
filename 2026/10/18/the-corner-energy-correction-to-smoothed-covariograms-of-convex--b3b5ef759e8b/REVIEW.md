# Independent mathematical audit

## correctness

PASS

The polar identity gives the factor K_p(z)=(p/2)(1-exp(-2A(z)/p)) integrated against r^2. With delta_i=p log(1+a_i/p), K_p(delta_i)=A(a_i)+E(a_i)/(2p)+O(p^-2), uniformly for bounded a_i. Over the old full edge sectors the radial area weights are 2W_i. For a switching strip let i be the old active edge, j the new, r_i and r_j their unshifted radial candidates, and s=p log(r_j/r_i). The strip is exactly 0<=s<=delta_i-delta_j, so the old edge has the larger scaled increment, the real argument is delta_j+s, and the reference argument is delta_i. The ratio log(r_j/r_i) has nonzero angular derivative of absolute value kappa at the vertex, with no other competing facet nearby. After this change of variables the factor r^2/|d log(r_j/r_i)/d theta| is Gamma_i+O(p^-1) uniformly there. Thus the correction is Gamma_i/p times the integral of A from the smaller to larger a minus the constant A at the larger a, up to O(p^-2). The argument also covers coalescing endpoints; all strip lengths in s are uniformly bounded and the original angular widths are O(p^-1). Summing finitely many sectors gives the compact-uniform error, and the normal balance cancels the linear part of A. Strict decrease of A gives J>=0 and equality only for equal arguments. If all a_i agree then their positively weighted sum is zero by normal balance, so all vanish; the spanning normals force y=0. Taylor expansion gives E=-z^4/32+O(z^5) and J=(a-b)^2/4+O((|a|+|b|)^3). If u=min(a,b) and v=max(a,b), A(-s)=A(s)+s yields J(a,b)-J(-a,-b)=(v-u)(A(u)-A(v))-(v-u)^2/2. Its cubic term is -(u+v)(v-u)^2/8 with fifth-order error. The stated triangle has facet parameters (-t,2t,-t) and all Gamma_i=1, giving the claimed -9t^3/4 with bulk odd error O(t^5).

## originality

PASS

The leading log-cosh term and a critical-rate order bound are already covered. The distinct supported claim is the full coefficient of 1/p for fixed polygons, including the vertex-switching integrals, the positive definite quadratic corner energy, and the explicit odd term. The inspected claims give no equivalent next-order coefficient.

## value

PASS

The first-order theory cannot distinguish effects confined to shrinking vertex sectors. The formula isolates their exact contribution, with a positive quadratic form dominating the quartic bulk term near zero. The explicit asymmetry demonstrates a qualitative feature of the finite-p radial smoothing that the even first limit does not see. These are substantive quantitative refinements for fixed polygons rather than just a smaller error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
