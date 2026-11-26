# Independent mathematical audit

## correctness

PASS

Regeneration with the whole state refreshed gives a unique stationary mixture over Exp(R) excursion ages. Integrating the linear velocity equation yields an independent translational Gaussian with per-coordinate variance v(t)=ct^3(1+O(t)), c=2/(3M^2); Maxwell initial velocity adds w^2 K(t)^2 and gives variance w^2t^2(1+O(t)). The bounded active displacement is O(t^2) and has mean Pe t^2 e_1/(2M)+O(t^(5/2)), using E|U_u-e_1|=O(sqrt(u)). An independent error check uses the Gaussian Taylor expansion in displacement: for |h|=O(t^2), |se-h|^2 >= s^2/2-|h|^2 and |h|^2/v(t)=O(t), so shifted derivatives retain a Gaussian cutoff. For zero reset velocity the Hessian term is at most O(t^(-2) exp(-c' s^2/t^3)); so are the leading-variance and age-weight errors, after absorbing Gaussian polynomial factors. The mean-error term is O(s t^(-7/2) exp(-c' s^2/t^3)); replacing the variance and age weight in the linear drift costs O(s t^(-3) exp(-c' s^2/t^3)). The integrated total is O(s^(-2/3)). Integrating the unshifted t^(-3) kernel gives A, and the linear t^(-4) kernel times s gives R Pe M/(4 pi) times (e dot e_1)/s. For Maxwell reset velocity, the corresponding variance and weight errors integrate a t^(-1) cutoff, hence give O(1+|log s|), and the displacement terms give O(1); the leading t^(-2) kernel gives C. Ages bounded away from zero contribute O(1). Exact convex mixing keeps the bounds uniform in p and e, including Pe=0 and both pure protocols. Substituting s=kappa p^3 gives the claimed density limit. Polar integration cancels the dipole in disk mass and gives the angular numerator pi B epsilon e_1, with denominator 3 pi A epsilon^(2/3) to leading order. Each positive age has a density, so there is no atom. In the proof f_0 denotes the zero-velocity component, not the p=0 mixture endpoint. I inspected the frozen numerical checker and its stated record; it is passive/linear-response corroboration, not a proof for arbitrary Pe, and was not rerun.

## originality

PASS

The supported distinction is the joint planar local-density expansion with the explicit active dipole at finite propulsion, uniform estimates for the two restoration protocols, and their rare-zero-velocity mixture consequences. The inertial active model, its complete zero-velocity resetting protocol, the renewal method, and related passive or marginal singularities are prior. The passive planar powers themselves have a direct dimension-scaling explanation and are not the sole basis of this judgment.

## value

PASS

The planar local mass and first orientation bias are natural observables inaccessible from the existing moment diagrams. The exact dipole shows how a reset heading survives below a leading isotropic singularity, and the uniform expansion separates effects of two experimentally distinct velocity-restoration rules. The cubic balance is informative because it gives both pointwise density and disk mass in the joint limit, although the balance itself is elementary once the endpoint expansions are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
