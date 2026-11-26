# Independent mathematical audit

## correctness

PASS

An independent slice calculation partitions generic directions into the 12 equiprobable ordered winner/runner pairs. For winner v_1 and runner v_2, use s=(U_2+U_3)/sqrt(2), w=sqrt(1−s²), U_1=w cos φ and (U_2−U_3)/sqrt(2)=w sin φ. Then Δ=κs, s≥0, and v_2 beats the other two exactly when U_1≥max(U_2,U_3), or w(sqrt(2)cos φ−|sin φ|)≥s. The angular interval has length 2H(s) up to s=sqrt(2/3); the surface element is ds dφ. Multiplying by 12/(4π) gives 6H(s)/π and rescaling gives the density. H'<0 on the interior; the stated primitive has derivative H and normalizes at the upper endpoint. Integration by parts gives the moment integrals; for the first use s=(sqrt(3)/2)sin θ and for the second z=sqrt(3−4s²), obtaining respectively arcsin(1/3) and π/6−1/(2sqrt(3)) for the integrals in the frozen proof. The nearest losing hemisphere has distance equal to the minimum over the three separating great circles; any path exiting the cell meets its boundary first, so inactive circle portions cannot give a smaller distance. Equal edge lengths make this distance arcsin(Δ/κ), giving the stated endpoint and the tail law; equality of the perturbation radius is immaterial in probability because there are no atoms. An independent direct sphere quadrature with 1024×2048 nodes found mean 0.529939262962 and second moment 0.398818370894, versus 0.529939502485 and 0.398818759625 analytically. CDF error at the four tested thresholds was at most 1.02×10^{-4} (finite-grid boundary error, not proof). Replay: /workspace/branches/9bd2fe8d-49a5-491b-8a41-8579561278d1/record5_quadrature.py and record5_quadrature_notes.txt. The frozen checker and recorded results were inspected, not executed.

## originality

PASS

The strongest inspected geometric and spacing results address a local clearance tail, a different order statistic, different sampling, or two-query collisions. A general spherical boundary integral and an explicit two-cap formula were inspected but do not evaluate the three-cap area needed here. The supported distinct content is the full one-query margin distribution and moments (and hence the exact radius distribution), not the general margin-to-hyperplane relation in isolation.

## value

PASS

The regular tetrahedron is a natural spherical nearest-vertex code, and the full distribution of its top gap tells exactly what surface fraction is robust against all perturbations at each angular radius. The formula supplies a usable benchmark from ties to maximal clearance, including a strictly decreasing margin density and moment values, not just one geometrical distance or endpoint estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
