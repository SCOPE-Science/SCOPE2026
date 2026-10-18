# Independent mathematical audit

## correctness

PASS

Reconstructed the exact sign-switched affine two-state update A=[[1-s,-alpha*beta],[(1-beta)*lambda,beta]], q=[-s*rho,(1-beta)*lambda*rho], trace(A)=1+beta-s, determinant(A)=beta. The alternating symmetry z_-=-z_+ follows from det(I-A)=s>0, while det(I+A)=2(1+beta)-s gives c=s*rho/[2(1+beta)-s]. Sign consistency and the three Jury inequalities agree exactly on 0<s<2(1+beta); the 2-step Jacobian is A^2. The determinant bound and discriminant yield minimal one-step modulus sqrt(beta) on the claimed closed band. For m_{-1}=0 and s>=2(1+beta), the magnitude recurrence y_{t+1}=(s-1-beta)y_t-beta*y_{t-1}+s*rho starts increasing: at equality increments obey d_{t+1}=beta*d_t+2(1+beta)*rho, above equality they grow geometrically. Independently checked orbit equations with exact rational beta in {0,1/3,2/3}, several s, and independent sign conventions. This proves only the fixed-preconditioner scalar deterministic case, not adaptive or stochastic SAM.

## originality

PASS

Best-of-knowledge PASS for the precise combined EMA momentum SAM orbit/stability/divergence theorem. Ordinary heavy-ball Jury inequalities are classical but do not alone supply the SAM sign-consistent forced orbit and standard-initialization sharp boundary; closest SAM primary sources analyze zero-momentum cycles, stochastic diffusion, adaptive stochastic bounds, or a different momentum perturbation. A hidden switched-affine/heavy-ball equivalent remains plausible.

## value

PASS

An exact existence/stability, amplitude and spectral-rate phase diagram is a useful benchmark for sign-oscillatory practical SAM with normalized EMA momentum. It identifies a sharp discrete switching boundary and distinguished local optimization band that are not a mere raw application of the no-momentum scalar theory. The scalar restriction bounds the significance but does not eliminate motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
