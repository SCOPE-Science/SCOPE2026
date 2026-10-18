# Independent mathematical audit

## correctness

PASS

For u'=u(r/(1+kv+alpha u)-a u-b v), v'=v(cb u-m-eta v) with all required positive params, logistic comparisons imply global positive boundedness. Prey-only root u1 of a u1(1+alpha u1)=r and threshold R=cb u1/m depend on no k; v extinction for R<=1 follows logistic upper comparison and u->u1 by lower comparison. When R>1, decreasing prey nullcline along predator nullcline gives a unique positive equilibrium with stable Jacobian; Dulac 1/(uv) has strictly negative divergence, ruling out positive periodic cycles, while boundary stable manifolds and directed boundary heteroclinic structure exclude other omega limits. At R=1, exact w=u-u1 equation w'=-u[A(u,v)w+B(u,v)v] gives p=w/v solving stable nonautonomous linear ODE tending -B/A, hence (1/v)'=eta-cb p->Q=eta+cb B/A and t v->1/Q, t(u1-u)->B/(A Q). Independent symbolic identities checked entire algebra, including dQ/dk>0, d(B/(A Q))/dk>0. Rigorous result only for this autonomous integer-order model and positive initial conditions.

## originality

PASS

Ramraj–Poornima's same-model Frontiers 2026 article provides the ODE and local equilibrium analysis and numerical convergence, while explicitly discussing future rigorous global stability. It does not state the all-parameter convergence proof or universal critical t^-1 coefficient. Resultary semantic searches of fear/refuge predator threshold yielded models with extra species, delays, or different functional responses, none implying the exact current Q coefficient. General Dulac and center-manifold methods are background, not new theorems by themselves.

## value

PASS

For a biologically motivated model, it closes the nonlinear global boundary including its nonhyperbolic critical case, and supplies an exact initial-condition-independent extinction clock and opposing fear responses at a fixed invasion threshold. The sharp critical coefficient distinguishes mathematical risk and time scale when threshold R alone is unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
