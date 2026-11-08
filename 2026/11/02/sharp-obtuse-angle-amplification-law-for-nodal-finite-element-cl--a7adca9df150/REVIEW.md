# Independent mathematical audit

## correctness

PASS

Apply affine spatial change z->D^{-1/2}z to reduce fixed SPD diffusion to Euclidean metric and sort three nodal values x_i<=x_j<=x_k. Gradients are v=-r grad lambda_i,w=s grad lambda_k with nonnegative r,s; middle-vertex angle theta_j between v,w. For monotone 1-Lipschitz g, new slopes are alpha v+beta w with alpha,beta∈[0,1]. Convexity of squared norm on square bounds by its four corners. For obtuse theta, completing squares proves ||v+w||²>=||v||²sin²theta and >=||w||²sin²theta; nonobtuse theta gives contraction. Explicit clipped sharpness chooses r,s so W=-V cos theta and saturates csc²theta; bounded and one-sided clipping can choose small preserved gaps. Exact 120° stiffness witness ratio4/3 verified independently, along with sampled nodal inequalities. Distinguish pointwise clipping (always contraction) and local P1 nodal clipping; no globally attained mesh coefficient asserted.

## originality

PASS

Previously proved 1D nodal cutoff H1 contraction uses ordered adjacent differences; planar angle geometry is not covered. Kreuzer pointwise FE cutoff is a different transform; Huang anisotropic D-metric mesh criteria address discrete maximum principles not the energy amplification supremum. The present sharp csc²θ law and explicit local attainability across SPD tensors survive statement-level comparisons. Older obscure local stiffness norm lemmas remain possible.

## value

PASS

Nodal truncation for maximum principles is standard, yet local energy stability on obtuse anisotropic triangles differs sharply from one-dimensional or pointwise-truncation contraction. A complete dimensionless csc²(metric angle) law and attainable worst case quantify mesh deterioration and provide an exact local finite-element stability guarantee. It does not assert global sharpness on assembled meshes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
